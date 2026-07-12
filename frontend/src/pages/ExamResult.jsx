import React, { useState } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import QuestionCard from '../components/QuestionCard';
import { 
  Trophy, CheckCircle, XCircle, Clock, 
  ArrowLeft, BarChart3, ChevronRight 
} from 'lucide-react';

export function ExamResult() {
  const location = useLocation();
  const navigate = useNavigate();

  // Retrieve results data from routing state
  const state = location.state || {};
  const { resultData, subject, examType, topic } = state;

  if (!resultData) {
    return (
      <div className="max-w-md mx-auto py-20 text-center space-y-4">
        <h3 className="text-lg font-bold text-slate-800 dark:text-slate-100">Không tìm thấy kết quả làm bài</h3>
        <button
          onClick={() => navigate('/exam')}
          className="px-6 py-2 rounded-xl bg-brand-600 text-white text-sm font-semibold hover:bg-brand-700 transition-colors"
        >
          Làm đề mới
        </button>
      </div>
    );
  }

  // State to filter review list
  const [filter, setFilter] = useState('all'); // all, correct, incorrect

  const gradedQuestions = resultData.graded_questions || [];

  const filteredQuestions = gradedQuestions.filter((q) => {
    if (filter === 'correct') return q.is_correct;
    if (filter === 'incorrect') return !q.is_correct;
    return true;
  });

  const formatTime = (totalSeconds) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins} phút ${secs} giây`;
  };

  const scoreColor = resultData.score >= 8.0 
    ? 'text-emerald-600 dark:text-emerald-400' 
    : resultData.score >= 5.0 
    ? 'text-brand-600 dark:text-brand-400' 
    : 'text-rose-600 dark:text-rose-400';

  return (
    <div className="space-y-8">
      {/* Page Header */}
      <div>
        <h1 className="text-2xl font-extrabold text-slate-800 dark:text-slate-100">Kết quả bài thi</h1>
        <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">Chúc mừng bạn đã hoàn thành bài thi thử!</p>
      </div>

      {/* Score Summary Card */}
      <div className="bg-white dark:bg-slate-800 rounded-3xl p-6 md:p-8 shadow-sm border border-slate-100 dark:border-slate-700/50 grid grid-cols-1 md:grid-cols-4 gap-6 items-center">
        
        {/* Big Score Radial/Box */}
        <div className="md:col-span-1 flex flex-col items-center justify-center p-6 border-b md:border-b-0 md:border-r border-slate-100 dark:border-slate-700">
          <div className="p-3 bg-brand-50 text-brand-600 dark:bg-brand-950/30 dark:text-brand-400 rounded-2xl mb-3">
            <Trophy className="w-8 h-8" />
          </div>
          <div className={`text-4xl font-black ${scoreColor}`}>
            {resultData.score}
          </div>
          <div className="text-xs font-semibold text-slate-400 dark:text-slate-500 mt-1 uppercase tracking-widest">
            Điểm số (Thang 10)
          </div>
        </div>

        {/* Stats Row */}
        <div className="md:col-span-3 grid grid-cols-3 gap-4 text-center">
          {/* Correct Answers */}
          <div className="space-y-1">
            <div className="inline-flex p-2 bg-emerald-50 text-emerald-600 dark:bg-emerald-950/20 dark:text-emerald-400 rounded-xl">
              <CheckCircle className="w-5 h-5" />
            </div>
            <div className="text-xl font-extrabold text-slate-800 dark:text-slate-100">
              {resultData.correct_answers} / {resultData.total_questions}
            </div>
            <div className="text-xs text-slate-400 dark:text-slate-500 font-medium">Câu trả lời đúng</div>
          </div>

          {/* Wrong Answers */}
          <div className="space-y-1">
            <div className="inline-flex p-2 bg-rose-50 text-rose-600 dark:bg-rose-950/20 dark:text-rose-400 rounded-xl">
              <XCircle className="w-5 h-5" />
            </div>
            <div className="text-xl font-extrabold text-slate-800 dark:text-slate-100">
              {resultData.total_questions - resultData.correct_answers}
            </div>
            <div className="text-xs text-slate-400 dark:text-slate-500 font-medium">Câu làm sai</div>
          </div>

          {/* Time spent */}
          <div className="space-y-1">
            <div className="inline-flex p-2 bg-slate-50 text-slate-600 dark:bg-slate-700/50 dark:text-slate-400 rounded-xl">
              <Clock className="w-5 h-5" />
            </div>
            <div className="text-lg font-extrabold text-slate-800 dark:text-slate-100">
              {formatTime(resultData.time_spent)}
            </div>
            <div className="text-xs text-slate-400 dark:text-slate-500 font-medium">Thời gian làm</div>
          </div>
        </div>

      </div>

      {/* Action shortcuts */}
      <div className="flex flex-wrap gap-3">
        <button
          onClick={() => navigate('/exam', { state: { subject } })}
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-bold text-sm shadow-md transition-colors"
        >
          Làm đề thi mới
        </button>
        <button
          onClick={() => navigate('/statistics')}
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 text-slate-700 dark:text-slate-200 font-bold text-sm shadow-sm transition-colors"
        >
          <BarChart3 className="w-4 h-4" /> Xem biểu đồ thống kê
        </button>
        <button
          onClick={() => navigate('/')}
          className="inline-flex items-center gap-2 px-5 py-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700 text-slate-600 dark:text-slate-300 font-semibold text-sm transition-colors"
        >
          <ArrowLeft className="w-4 h-4" /> Quay lại trang chủ
        </button>
      </div>

      {/* Review Section Filters */}
      <div className="space-y-6">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 border-b border-slate-200 dark:border-slate-800 pb-3">
          <h2 className="text-lg font-bold text-slate-800 dark:text-slate-100">Xem lại câu hỏi</h2>
          
          <div className="flex gap-1.5 p-1 bg-slate-100 dark:bg-slate-800 rounded-xl">
            {[
              { id: 'all', name: 'Tất cả' },
              { id: 'correct', name: 'Câu đúng' },
              { id: 'incorrect', name: 'Câu sai' }
            ].map((btn) => (
              <button
                key={btn.id}
                onClick={() => setFilter(btn.id)}
                className={`px-4 py-1.5 rounded-lg text-xs font-bold transition-all ${
                  filter === btn.id
                    ? 'bg-white dark:bg-slate-700 text-slate-800 dark:text-white shadow-sm'
                    : 'text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'
                }`}
              >
                {btn.name}
              </button>
            ))}
          </div>
        </div>

        {/* Display Graded QuestionCards */}
        <div className="space-y-6">
          {filteredQuestions.map((q) => (
            <QuestionCard
              key={q.id}
              question={q}
              selectedAnswer={q.selected_answer}
              showAnswer={true}
              isBookmarked={false} // Disable bookmark toggles on results review page
            />
          ))}
          {filteredQuestions.length === 0 && (
            <div className="bg-white dark:bg-slate-800 rounded-2xl p-12 border border-slate-100 dark:border-slate-700/50 text-center text-slate-400">
              Không có câu hỏi nào tương ứng với bộ lọc đã chọn.
            </div>
          )}
        </div>
      </div>

    </div>
  );
}

export default ExamResult;
