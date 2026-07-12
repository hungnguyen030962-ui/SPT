import React from 'react';
import { Link } from 'react-router-dom';
import { 
  Play, BookOpen, Bookmark, FileText, 
  CheckCircle, ArrowRight, BarChart3, AlertCircle, RefreshCw
} from 'lucide-react';

export function Home() {
  // Load data from localStorage
  const attempts = JSON.parse(localStorage.getItem('spt_exam_attempts') || '[]');
  const bookmarks = JSON.parse(localStorage.getItem('spt_bookmarks') || '[]');
  const wrongQuestions = JSON.parse(localStorage.getItem('spt_wrong_questions') || '[]');
  const learnedCards = JSON.parse(localStorage.getItem('spt_flashcard_learned') || '[]');

  // Calculate statistics
  const totalAttempts = attempts.length;
  const avgScore = totalAttempts > 0 
    ? (attempts.reduce((sum, item) => sum + item.score, 0) / totalAttempts).toFixed(1) 
    : '0.0';
  
  // Total questions solved in exams
  const totalSolved = attempts.reduce((sum, item) => sum + item.total_questions, 0);
  const totalCorrect = attempts.reduce((sum, item) => sum + item.correct_answers, 0);
  const correctRate = totalSolved > 0 
    ? ((totalCorrect / totalSolved) * 100).toFixed(0) 
    : '0';

  const stats = [
    { name: 'Bài thi đã làm', value: totalAttempts, icon: FileSpreadsheetIcon, color: 'bg-blue-500 text-white' },
    { name: 'Điểm trung bình', value: `${avgScore}/10`, icon: CheckCircle, color: 'bg-emerald-500 text-white' },
    { name: 'Câu hỏi đã làm', value: totalSolved, icon: BookOpen, color: 'bg-purple-500 text-white' },
    { name: 'Tỉ lệ đúng', value: `${correctRate}%`, icon: BarChart3, color: 'bg-amber-500 text-white' },
  ];

  return (
    <div className="space-y-10">
      {/* Hero Welcome Banner */}
      <div className="relative overflow-hidden rounded-3xl bg-gradient-to-r from-brand-600 to-blue-500 px-8 py-10 text-white shadow-xl shadow-brand-600/10">
        {/* Glow Effects */}
        <div className="absolute right-0 top-0 -mr-16 -mt-16 w-80 h-80 bg-white/10 rounded-full blur-2xl pointer-events-none" />
        <div className="absolute left-1/3 bottom-0 -mb-20 w-60 h-60 bg-blue-400/20 rounded-full blur-2xl pointer-events-none" />

        <div className="relative z-10 max-w-2xl">
          <span className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-white/20 text-xs font-semibold uppercase tracking-wider mb-4">
            🚀 Ôn thi cấp tốc ĐGNL HNUE
          </span>
          <h1 className="text-3xl md:text-4xl font-extrabold tracking-tight mb-3">
            Hệ thống luyện thi SPT HNUE
          </h1>
          <p className="text-blue-100 text-sm md:text-base mb-6 leading-relaxed">
            Nền tảng thi thử trực tuyến hoàn chỉnh môn Toán học. Không cần đăng nhập, vào làm bài ngay lập tức, lời giải chi tiết và phân tích tiến độ thông minh.
          </p>
          <div className="flex flex-wrap gap-3">
            <Link
              to="/exam"
              className="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-white text-brand-600 hover:bg-slate-50 font-bold text-sm shadow-md transition-all hover:translate-x-0.5"
            >
              <Play className="w-4 h-4 fill-brand-600" /> Bắt đầu làm đề
            </Link>
          </div>
        </div>
      </div>

      {/* Quick Statistics Row */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-4">
        {stats.map((stat, index) => (
          <div 
            key={index} 
            className="bg-white dark:bg-slate-800 p-5 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700/50 flex items-center gap-4"
          >
            <div className={`p-3 rounded-xl ${stat.color} shrink-0`}>
              <stat.icon className="w-6 h-6" />
            </div>
            <div>
              <p className="text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">{stat.name}</p>
              <h3 className="text-xl font-extrabold text-slate-800 dark:text-slate-100 mt-0.5">{stat.value}</h3>
            </div>
          </div>
        ))}
      </div>

      {/* Main Sections Link Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        {/* Math & Science card */}
        <div className="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700/50 p-6 rounded-2xl shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
          <div>
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-blue-100 text-blue-600 dark:bg-blue-950/50 dark:text-blue-400 mb-4 font-bold text-xl">
              ∑
            </div>
            <h3 className="text-lg font-bold text-slate-800 dark:text-slate-100 mb-2">Đề thi thử Toán học</h3>
            <p className="text-slate-500 dark:text-slate-400 text-sm leading-relaxed mb-6">
              Luyện tập các đề thi thử ĐGNL môn Toán chuẩn cấu trúc HNUE. Hỗ trợ hiển thị công thức LaTeX trực quan và cung cấp lời giải chi tiết từng bước.
            </p>
          </div>
          <Link
            to="/exam?subject=math"
            className="flex items-center gap-1.5 text-sm font-bold text-brand-600 dark:text-brand-400 hover:gap-2.5 transition-all mt-auto"
          >
            Vào làm đề Toán <ArrowRight className="w-4 h-4" />
          </Link>
        </div>

        {/* Review & Revision card */}
        <div className="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700/50 p-6 rounded-2xl shadow-sm hover:shadow-md transition-all flex flex-col justify-between">
          <div>
            <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-rose-100 text-rose-600 dark:bg-rose-950/50 dark:text-rose-400 mb-4">
              <RefreshCw className="w-6 h-6" />
            </div>
            <h3 className="text-lg font-bold text-slate-800 dark:text-slate-100 mb-2">Trung tâm ôn tập</h3>
            <p className="text-slate-500 dark:text-slate-400 text-sm leading-relaxed mb-6">
              Xem lại các câu hỏi đã lưu, xem danh sách các câu làm sai và thực hiện luyện tập lại để củng cố kiến thức còn yếu.
            </p>
          </div>
          <Link
            to="/review"
            className="flex items-center gap-1.5 text-sm font-bold text-brand-600 dark:text-brand-400 hover:gap-2.5 transition-all mt-auto"
          >
            Vào trung tâm ôn tập <ArrowRight className="w-4 h-4" />
          </Link>
        </div>
      </div>

      {/* Review Section Shortcuts */}
      <div className="bg-slate-100 dark:bg-slate-800/40 rounded-2xl p-6 border border-slate-200/50 dark:border-slate-800 flex flex-col md:flex-row items-center justify-between gap-6">
        <div className="flex items-start gap-4">
          <div className="p-3 bg-rose-100 text-rose-600 dark:bg-rose-950/40 dark:text-rose-400 rounded-xl shrink-0">
            <AlertCircle className="w-6 h-6" />
          </div>
          <div>
            <h3 className="text-base font-bold text-slate-800 dark:text-slate-100">Khu vực sửa sai & Lưu trữ</h3>
            <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">
              Bạn đang có <strong className="text-rose-600 dark:text-rose-400">{wrongQuestions.length} câu làm sai</strong> và <strong className="text-brand-600 dark:text-brand-400">{bookmarks.length} câu đã đánh dấu</strong>. Hãy ôn tập lại thường xuyên để củng cố kiến thức.
            </p>
          </div>
        </div>
        <Link
          to="/review"
          className="px-5 py-2.5 rounded-xl bg-white dark:bg-slate-800 border border-slate-200 dark:border-slate-700 hover:bg-slate-50 text-sm font-bold shadow-sm transition-colors text-slate-700 dark:text-slate-200"
        >
          Mở trung tâm ôn tập
        </Link>
      </div>

    </div>
  );
}

// Simple Helper Icon components
function FileSpreadsheetIcon(props) {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" {...props}>
      <path d="M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z"/>
      <path d="M14 2v4a2 2 0 0 0 2 2h4"/>
      <path d="M8 13h8"/>
      <path d="M8 17h8"/>
      <path d="M8 9h2"/>
    </svg>
  );
}

export default Home;
