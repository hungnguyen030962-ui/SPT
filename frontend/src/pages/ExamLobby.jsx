import React, { useEffect, useState } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import examService from '../services/examService';
import { Play, Sparkles, BookOpen, Clock, Layers } from 'lucide-react';

export function ExamLobby() {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  // Selected config
  const [subject, setSubject] = useState(searchParams.get('subject') || 'math');
  const [examType, setExamType] = useState('random'); // topic, random, full
  const [examName, setExamName] = useState('Đề số 1'); // fixed exams for math
  const [topic, setTopic] = useState('');
  const [limit, setLimit] = useState(10);
  const [timeLimit, setTimeLimit] = useState(20); // in minutes

  const [topicsMap, setTopicsMap] = useState({});
  const [loadingTopics, setLoadingTopics] = useState(true);

  useEffect(() => {
    const fetchTopics = async () => {
      try {
        const data = await examService.getTopics();
        setTopicsMap(data);
      } catch (err) {
        console.error("Error loading topics:", err);
      } finally {
        setLoadingTopics(false);
      }
    };
    fetchTopics();
  }, []);

  // Update time limit dynamically when question limit changes (2 mins per question as guideline)
  useEffect(() => {
    if (subject !== 'math') {
      setTimeLimit(limit * 2);
    }
  }, [limit, subject]);

  // Adjust topics when subject changes
  const activeTopics = topicsMap[subject] || [];

  const handleStartExam = () => {
    const finalExamType = subject === 'math' ? 'full' : examType;
    const finalLimit = subject === 'math' ? 50 : limit;
    const finalTimeLimit = subject === 'math' ? 90 * 60 : timeLimit * 60; // Math has fixed 90 mins
    const finalTopic = subject === 'math' ? '' : (examType === 'topic' ? topic : '');
    const finalExamName = subject === 'math' ? examName : '';

    navigate('/exam/active', {
      state: {
        subject,
        examType: finalExamType,
        examName: finalExamName,
        topic: finalTopic,
        limit: finalLimit,
        timeLimit: finalTimeLimit,
      }
    });
  };

  return (
    <div className="max-w-3xl mx-auto space-y-8">
      <div>
        <h1 className="text-2xl font-extrabold text-slate-800 dark:text-slate-100">Luyện thi & Đề thi</h1>
        <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">
          Thiết lập cấu hình đề thi thử của bạn: chọn môn, chuyên đề, thời gian làm bài.
        </p>
      </div>

      <div className="bg-white dark:bg-slate-800 rounded-3xl p-6 md:p-8 shadow-sm border border-slate-100 dark:border-slate-700/50 space-y-6">
        
        {/* Step 1: Chọn đề thi môn Toán (HNUE) */}
        <div className="space-y-3">
          <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
            Chọn đề thi thử môn Toán (HNUE)
          </label>
          <div className="grid grid-cols-2 sm:grid-cols-3 gap-3">
            {["Đề số 1", "Đề số 2", "Đề số 3", "Đề số 4", "Đề số 5", "Đề số 6"].map((name) => {
              const isSelected = examName === name;
              return (
                <button
                  key={name}
                  type="button"
                  onClick={() => setExamName(name)}
                  className={`flex flex-col items-center justify-center p-5 rounded-2xl border text-center transition-all ${
                    isSelected
                      ? 'border-brand-600 bg-brand-50/30 text-brand-700 dark:border-brand-500 dark:bg-brand-950/20 dark:text-brand-400 ring-2 ring-brand-600/10'
                      : 'border-slate-200 hover:bg-slate-50 dark:border-slate-700 dark:hover:bg-slate-700/30 text-slate-700 dark:text-slate-300'
                  }`}
                >
                  <BookOpen className="w-5 h-5 mb-2 text-brand-500" />
                  <span className="font-bold text-sm">{name}</span>
                  <span className="text-xs text-slate-400 dark:text-slate-500 mt-0.5">90 phút • 38 câu hỏi</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Step 2: Thông tin đề thi */}
        <div className="p-5 rounded-2xl bg-blue-50/30 dark:bg-slate-900/30 border border-blue-100/30 dark:border-slate-700/50 text-sm text-slate-600 dark:text-slate-400">
          <span className="font-bold text-brand-700 dark:text-brand-400 block mb-1">Thông tin đề thi thử môn Toán:</span>
          Thời gian làm bài là **90 phút**. Đề thi gồm 38 câu hỏi trắc nghiệm khách quan, trắc nghiệm đúng/sai và tự luận trả lời ngắn chuẩn cấu trúc tuyển sinh Đại học Sư phạm Hà Nội. Kết quả và bảng điểm chi tiết kèm lời giải từng bước sẽ được hiển thị ngay sau khi nộp bài.
        </div>

        {/* Start Action Button */}
        <div className="pt-4 border-t border-slate-100 dark:border-slate-700/50 flex justify-end">
          <button
            onClick={handleStartExam}
            disabled={examType === 'topic' && !topic}
            className="w-full sm:w-auto inline-flex items-center justify-center gap-2 px-8 py-3.5 rounded-xl bg-brand-600 hover:bg-brand-700 disabled:opacity-50 disabled:pointer-events-none text-white font-bold text-sm shadow-lg shadow-brand-600/10 transition-colors"
          >
            <Play className="w-4 h-4 fill-white" /> Bắt đầu thi thử
          </button>
        </div>

      </div>
    </div>
  );
}

export default ExamLobby;
