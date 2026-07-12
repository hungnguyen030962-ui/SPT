import React, { useEffect, useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import examService from '../services/examService';
import QuestionCard from '../components/QuestionCard';
import CountdownTimer from '../components/CountdownTimer';
import useLocalStorage from '../hooks/useLocalStorage';
import { ArrowLeft, ArrowRight, CheckCircle, RefreshCw, AlertTriangle } from 'lucide-react';

export function ExamActive() {
  const location = useLocation();
  const navigate = useNavigate();

  // Redirect if no config was passed
  const config = location.state || {};
  const { subject, examType, topic, limit, timeLimit } = config;

  useEffect(() => {
    if (!subject) {
      navigate('/exam');
    }
  }, [subject, navigate]);

  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // User's selections
  const [answers, setAnswers] = useState({}); // {question_id: option}
  const [currentIdx, setCurrentIdx] = useState(0);
  
  // Track bookmarks
  const [bookmarks, setBookmarks] = useLocalStorage('spt_bookmarks', []);

  // Time tracking
  const [timeSpent, setTimeSpent] = useState(0);
  const [timerActive, setTimerActive] = useState(true);

  useEffect(() => {
    const fetchQuestions = async () => {
      setLoading(true);
      setError(null);
      try {
        const params = {
          subject,
          limit,
          hide_answers: true, // Hide answers during exam
        };
        if (topic) params.topic = topic;

        const data = await examService.getQuestions(params);
        if (data.length === 0) {
          setError("Không có đủ câu hỏi trong ngân hàng cho chuyên đề/môn học này. Vui lòng thiết lập cấu hình khác.");
        } else {
          setQuestions(data);
        }
      } catch (err) {
        console.error("Error fetching questions for exam:", err);
        setError("Không thể tải đề thi. Vui lòng kiểm tra lại kết nối mạng.");
      } finally {
        setLoading(false);
      }
    };

    if (subject) {
      fetchQuestions();
    }
  }, [subject, topic, limit]);

  // Keep track of time elapsed
  useEffect(() => {
    if (!timerActive) return;
    const interval = setInterval(() => {
      setTimeSpent(prev => prev + 1);
    }, 1000);
    return () => clearInterval(interval);
  }, [timerActive]);

  const handleSelectAnswer = (qId, option) => {
    setAnswers(prev => ({ ...prev, [qId]: option }));
  };

  const handleToggleBookmark = (qId) => {
    setBookmarks(prev => 
      prev.includes(qId) ? prev.filter(id => id !== qId) : [...prev, qId]
    );
  };

  const handleAutoSubmit = () => {
    alert("Hết giờ làm bài! Hệ thống đang tự động nộp bài thi.");
    submitTest();
  };

  const submitTest = async () => {
    setTimerActive(false);
    setLoading(true);
    try {
      const response = await examService.submitExam(answers, timeSpent);
      
      // 1. Save attempt to localStorage
      const attempt = {
        id: Date.now().toString(),
        subject,
        exam_type: examType,
        topic,
        score: response.score,
        total_questions: response.total_questions,
        correct_answers: response.correct_answers,
        time_spent: response.time_spent,
        created_at: new Date().toISOString(),
      };
      
      const existingAttempts = JSON.parse(localStorage.getItem('spt_exam_attempts') || '[]');
      existingAttempts.push(attempt);
      localStorage.setItem('spt_exam_attempts', JSON.stringify(existingAttempts));

      // 2. Save wrong answers to localStorage for review
      const wrongList = JSON.parse(localStorage.getItem('spt_wrong_questions') || '[]');
      response.graded_questions.forEach(q => {
        if (!q.is_correct) {
          // If not already in wrong list, add it
          if (!wrongList.includes(q.id)) {
            wrongList.push(q.id);
          }
        } else {
          // If correct and existed in wrong list, remove it
          const idx = wrongList.indexOf(q.id);
          if (idx > -1) {
            wrongList.splice(idx, 1);
          }
        }
      });
      localStorage.setItem('spt_wrong_questions', JSON.stringify(wrongList));

      // 3. Navigate to results page
      navigate('/exam/result', { state: { resultData: response, subject, examType, topic } });
    } catch (err) {
      console.error("Error submitting test:", err);
      alert("Đã xảy ra lỗi khi nộp bài. Vui lòng thử lại.");
      setTimerActive(true);
      setLoading(false);
    }
  };

  const handleSubmitClick = () => {
    const unansweredCount = questions.length - Object.keys(answers).length;
    let message = "Bạn có chắc chắn muốn nộp bài?";
    if (unansweredCount > 0) {
      message = `Bạn còn ${unansweredCount} câu chưa làm. Bạn vẫn muốn nộp bài chứ?`;
    }
    
    if (window.confirm(message)) {
      submitTest();
    }
  };

  if (loading && questions.length === 0) {
    return (
      <div className="flex flex-col items-center justify-center py-32 gap-3">
        <RefreshCw className="w-8 h-8 text-brand-500 animate-spin" />
        <span className="text-slate-400 text-sm">Đang tải đề thi...</span>
      </div>
    );
  }

  if (error) {
    return (
      <div className="max-w-md mx-auto py-16 text-center space-y-4">
        <div className="inline-flex p-3 bg-rose-50 text-rose-500 rounded-2xl dark:bg-rose-950/20">
          <AlertTriangle className="w-6 h-6" />
        </div>
        <h3 className="text-lg font-bold text-slate-800 dark:text-slate-100">Không thể bắt đầu thi</h3>
        <p className="text-slate-500 dark:text-slate-400 text-sm leading-relaxed">{error}</p>
        <button
          onClick={() => navigate('/exam')}
          className="px-6 py-2 rounded-xl bg-brand-600 text-white text-sm font-semibold hover:bg-brand-700 transition-colors"
        >
          Quay lại thiết lập
        </button>
      </div>
    );
  }

  const currentQuestion = questions[currentIdx];

  return (
    <div className="grid grid-cols-1 lg:grid-cols-4 gap-8 items-start">
      
      {/* Left Area: Main Question card and navigation */}
      <div className="lg:col-span-3 space-y-6">
        
        {/* Navigation top bar */}
        <div className="flex items-center justify-between bg-white dark:bg-slate-800 px-6 py-3 rounded-2xl border border-slate-100 dark:border-slate-700/50 shadow-sm">
          <div className="text-sm font-bold text-slate-700 dark:text-slate-300">
            Câu {currentIdx + 1} / {questions.length}
          </div>
          
          <div className="flex items-center gap-2">
            <button
              onClick={() => setCurrentIdx(prev => Math.max(0, prev - 1))}
              disabled={currentIdx === 0}
              className="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 disabled:opacity-40 disabled:pointer-events-none"
            >
              <ArrowLeft className="w-4 h-4" />
            </button>
            <button
              onClick={() => setCurrentIdx(prev => Math.min(questions.length - 1, prev + 1))}
              disabled={currentIdx === questions.length - 1}
              className="p-1.5 rounded-lg border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 disabled:opacity-40 disabled:pointer-events-none"
            >
              <ArrowRight className="w-4 h-4" />
            </button>
          </div>
        </div>

        {/* The active QuestionCard */}
        {currentQuestion && (
          <QuestionCard
            question={currentQuestion}
            selectedAnswer={answers[currentQuestion.id]}
            onSelectAnswer={(opt) => handleSelectAnswer(currentQuestion.id, opt)}
            showAnswer={false}
            isBookmarked={bookmarks.includes(currentQuestion.id)}
            onToggleBookmark={handleToggleBookmark}
          />
        )}

        {/* Submit controls below card */}
        <div className="flex justify-between items-center bg-white dark:bg-slate-800 px-6 py-4 rounded-2xl border border-slate-100 dark:border-slate-700/50 shadow-sm">
          <span className="text-xs text-slate-400 dark:text-slate-500">
            Hãy kiểm tra kỹ toàn bộ đáp án trước khi nộp bài.
          </span>
          <button
            onClick={handleSubmitClick}
            className="inline-flex items-center gap-1.5 px-6 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-bold text-sm shadow-md transition-colors"
          >
            <CheckCircle className="w-4 h-4" /> Nộp bài thi
          </button>
        </div>

      </div>

      {/* Right Area: Sidebar control panel */}
      <div className="lg:col-span-1 space-y-6 lg:sticky lg:top-24">
        
        {/* Timer Box */}
        <div className="bg-white dark:bg-slate-800 p-5 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700/50 flex flex-col items-center gap-3">
          <div className="text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">Thời gian còn lại</div>
          {timeLimit && (
            <CountdownTimer
              initialSeconds={timeLimit}
              onTimeUp={handleAutoSubmit}
              isActive={timerActive}
            />
          )}
        </div>

        {/* Answer Sheet Index Grid */}
        <div className="bg-white dark:bg-slate-800 p-5 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700/50 space-y-4">
          <div className="text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider text-center">
            Phiếu trả lời
          </div>
          
          <div className="grid grid-cols-5 gap-2">
            {questions.map((q, idx) => {
              const isAnswered = answers[q.id] !== undefined;
              const isCurrent = currentIdx === idx;
              const isBookmarked = bookmarks.includes(q.id);

              let buttonStyle = "border-slate-200 dark:border-slate-700 text-slate-600 dark:text-slate-300";
              if (isAnswered) {
                buttonStyle = "bg-brand-100 border-brand-300 text-brand-700 dark:bg-brand-950/40 dark:border-brand-900 dark:text-brand-400";
              }
              if (isCurrent) {
                buttonStyle = "bg-brand-600 border-brand-600 text-white dark:bg-brand-600 dark:border-brand-600";
              }

              return (
                <button
                  key={q.id}
                  onClick={() => setCurrentIdx(idx)}
                  className={`w-10 h-10 border rounded-xl flex items-center justify-center font-bold text-sm relative transition-all ${buttonStyle}`}
                >
                  {idx + 1}
                  {isBookmarked && (
                    <span className="absolute top-0 right-0 w-2 h-2 rounded-full bg-amber-500" />
                  )}
                </button>
              );
            })}
          </div>

          <div className="pt-2 border-t border-slate-100 dark:border-slate-700/50 flex flex-wrap justify-between text-xs text-slate-400 gap-2">
            <span className="flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded bg-brand-600 inline-block" /> Đang làm
            </span>
            <span className="flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded bg-brand-100 dark:bg-brand-950/40 inline-block" /> Đã trả lời
            </span>
            <span className="flex items-center gap-1">
              <span className="w-2.5 h-2.5 rounded bg-amber-500 inline-block" /> Đánh dấu
            </span>
          </div>
        </div>

      </div>

    </div>
  );
}

export default ExamActive;
