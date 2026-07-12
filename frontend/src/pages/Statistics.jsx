import React, { useMemo } from 'react';
import { 
  LineChart, Line, XAxis, YAxis, 
  CartesianGrid, Tooltip, ResponsiveContainer, 
  BarChart, Bar, Legend 
} from 'recharts';
import { 
  BarChart3, Award, AlertCircle, 
  HelpCircle, ChevronRight, RefreshCw 
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export function Statistics() {
  const navigate = useNavigate();
  
  // Load attempts from localStorage
  const attempts = useMemo(() => {
    const data = JSON.parse(localStorage.getItem('spt_exam_attempts') || '[]');
    // Sort chronologically by date
    return data.sort((a, b) => new Date(a.created_at) - new Date(b.created_at));
  }, []);

  // 1. Calculate overall metrics
  const totalAttempts = attempts.length;
  
  const overallStats = useMemo(() => {
    const stats = {
      math: { count: 0, totalQ: 0, correctQ: 0, sumScore: 0 },
      literature: { count: 0, totalQ: 0, correctQ: 0, sumScore: 0 },
      english: { count: 0, totalQ: 0, correctQ: 0, sumScore: 0 }
    };

    attempts.forEach(item => {
      const sub = item.subject;
      if (stats[sub]) {
        stats[sub].count += 1;
        stats[sub].totalQ += item.total_questions;
        stats[sub].correctQ += item.correct_answers;
        stats[sub].sumScore += item.score;
      }
    });

    return stats;
  }, [attempts]);

  // 2. Identify Strong/Weak Topics
  // To identify topics, we parse attempts that have topics (e.g. topic examType)
  const topicStats = useMemo(() => {
    const topics = {};
    attempts.forEach(item => {
      if (item.exam_type === 'topic' && item.topic) {
        const key = item.topic;
        if (!topics[key]) {
          topics[key] = { total: 0, correct: 0, subject: item.subject };
        }
        topics[key].total += item.total_questions;
        topics[key].correct += item.correct_answers;
      }
    });

    const list = Object.entries(topics).map(([name, data]) => {
      const rate = data.total > 0 ? (data.correct / data.total) * 100 : 0;
      return { name, rate, subject: data.subject };
    });

    const strong = list.filter(t => t.rate >= 70);
    const weak = list.filter(t => t.rate < 70);

    return { strong, weak };
  }, [attempts]);

  // 3. Format chart data
  const chartData = useMemo(() => {
    return attempts.map((item, index) => {
      const date = new Date(item.created_at);
      return {
        name: `Đề ${index + 1}`,
        'Điểm': item.score,
        'Môn': item.subject === 'math' ? 'Toán' : item.subject === 'literature' ? 'Văn' : 'Anh',
        date: date.toLocaleDateString('vi-VN', { month: 'numeric', day: 'numeric' })
      };
    });
  }, [attempts]);

  const getSubjectLabel = (subKey) => {
    if (subKey === 'math') return 'Toán học';
    if (subKey === 'literature') return 'Ngữ văn';
    return 'Tiếng Anh';
  };

  const getAccuracy = (correct, total) => {
    return total > 0 ? ((correct / total) * 100).toFixed(0) : '0';
  };

  return (
    <div className="space-y-8">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-extrabold text-slate-800 dark:text-slate-100">Thống kê học tập</h1>
        <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">Đánh giá tiến độ điểm thi, điểm mạnh và điểm yếu qua từng đề làm thử.</p>
      </div>

      {totalAttempts === 0 ? (
        <div className="bg-white dark:bg-slate-800 rounded-3xl p-12 text-center text-slate-400 border border-slate-100 dark:border-slate-700/50 space-y-4 max-w-md mx-auto">
          <BarChart3 className="w-12 h-12 mx-auto text-slate-300 dark:text-slate-600" />
          <div>
            <h3 className="font-bold text-slate-700 dark:text-slate-300 text-lg">Chưa có dữ liệu thống kê</h3>
            <p className="text-sm mt-1">Hãy làm thử ít nhất 1 bài thi hoặc luyện tập chuyên đề để hệ thống tự động tổng hợp kết quả.</p>
          </div>
          <button
            onClick={() => navigate('/exam')}
            className="px-6 py-2.5 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-bold text-sm shadow-md transition-colors"
          >
            Làm bài ngay
          </button>
        </div>
      ) : (
        <>
          {/* Subject summaries */}
          <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
            {['math', 'literature', 'english'].map((subKey) => {
              const data = overallStats[subKey];
              const avg = data.count > 0 ? (data.sumScore / data.count).toFixed(1) : '0.0';
              const rate = getAccuracy(data.correctQ, data.totalQ);

              return (
                <div 
                  key={subKey} 
                  className="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700/50 rounded-2xl p-5 shadow-sm space-y-4"
                >
                  <div className="flex items-center justify-between">
                    <span className="font-extrabold text-slate-800 dark:text-slate-100 text-base">{getSubjectLabel(subKey)}</span>
                    <span className="text-xs font-semibold px-2 py-0.5 rounded-full bg-slate-100 text-slate-500 dark:bg-slate-700 dark:text-slate-400">
                      {data.count} lượt thi
                    </span>
                  </div>
                  
                  <div className="grid grid-cols-2 gap-4 pt-2 border-t border-slate-100 dark:border-slate-700/50">
                    <div>
                      <p className="text-xs text-slate-400 dark:text-slate-500 font-semibold uppercase tracking-wider">Điểm trung bình</p>
                      <h4 className="text-xl font-black text-brand-600 dark:text-brand-400 mt-0.5">{avg}/10</h4>
                    </div>
                    <div>
                      <p className="text-xs text-slate-400 dark:text-slate-500 font-semibold uppercase tracking-wider">Tỉ lệ đúng</p>
                      <h4 className="text-xl font-black text-emerald-600 dark:text-emerald-400 mt-0.5">{rate}%</h4>
                    </div>
                  </div>
                </div>
              );
            })}
          </div>

          {/* Progress Chart */}
          <div className="bg-white dark:bg-slate-800 p-6 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700/50">
            <h3 className="text-base font-bold text-slate-800 dark:text-slate-100 mb-6">Biểu đồ tiến độ điểm số</h3>
            <div className="h-80 w-full">
              <ResponsiveContainer width="100%" height="100%">
                <LineChart
                  data={chartData}
                  margin={{ top: 10, right: 30, left: 0, bottom: 0 }}
                >
                  <CartesianGrid strokeDasharray="3 3" vertical={false} stroke="#f1f5f9" />
                  <XAxis dataKey="name" stroke="#94a3b8" fontSize={11} tickLine={false} />
                  <YAxis domain={[0, 10]} stroke="#94a3b8" fontSize={11} tickLine={false} />
                  <Tooltip 
                    contentStyle={{ borderRadius: '12px', border: 'none', boxShadow: '0 4px 12px rgba(0,0,0,0.05)' }} 
                  />
                  <Line 
                    type="monotone" 
                    dataKey="Điểm" 
                    stroke="#2563eb" 
                    strokeWidth={3} 
                    dot={{ r: 5, stroke: '#2563eb', strokeWidth: 2, fill: '#fff' }}
                    activeDot={{ r: 7 }} 
                  />
                </LineChart>
              </ResponsiveContainer>
            </div>
          </div>

          {/* Strong / Weak Topics Analysis */}
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            
            {/* Strong Topics */}
            <div className="bg-white dark:bg-slate-800 p-6 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700/50 space-y-4">
              <div className="flex items-center gap-2 text-emerald-650 text-emerald-600 dark:text-emerald-400 border-b border-slate-100 dark:border-slate-700/50 pb-3">
                <Award className="w-5 h-5" />
                <h3 className="font-bold text-sm uppercase tracking-wider">Chuyên đề thế mạnh (>= 70%)</h3>
              </div>
              
              {topicStats.strong.length === 0 ? (
                <p className="text-sm text-slate-400 text-center py-6">Chưa ghi nhận chuyên đề thế mạnh nào.</p>
              ) : (
                <div className="space-y-3">
                  {topicStats.strong.map((t, idx) => (
                    <div key={idx} className="flex items-center justify-between text-sm py-1">
                      <span className="font-medium text-slate-700 dark:text-slate-350">{t.name} ({getSubjectLabel(t.subject)})</span>
                      <span className="font-bold text-emerald-600 dark:text-emerald-400">{t.rate.toFixed(0)}% đúng</span>
                    </div>
                  ))}
                </div>
              )}
            </div>

            {/* Weak Topics */}
            <div className="bg-white dark:bg-slate-800 p-6 rounded-3xl shadow-sm border border-slate-100 dark:border-slate-700/50 space-y-4">
              <div className="flex items-center gap-2 text-rose-650 text-rose-600 dark:text-rose-400 border-b border-slate-100 dark:border-slate-700/50 pb-3">
                <AlertCircle className="w-5 h-5" />
                <h3 className="font-bold text-sm uppercase tracking-wider">Chuyên đề cần cải thiện (&lt; 70%)</h3>
              </div>
              
              {topicStats.weak.length === 0 ? (
                <p className="text-sm text-slate-400 text-center py-6">Không ghi nhận chuyên đề yếu nào.</p>
              ) : (
                <div className="space-y-3">
                  {topicStats.weak.map((t, idx) => (
                    <div key={idx} className="flex items-center justify-between text-sm py-1">
                      <span className="font-medium text-slate-700 dark:text-slate-350">{t.name} ({getSubjectLabel(t.subject)})</span>
                      <span className="font-bold text-rose-600 dark:text-rose-400">{t.rate.toFixed(0)}% đúng</span>
                    </div>
                  ))}
                </div>
              )}
            </div>

          </div>

          {/* Reset Stats Control */}
          <div className="text-center pt-4">
            <button
              onClick={() => {
                if (window.confirm("Bạn có chắc chắn muốn xóa toàn bộ lịch sử thi và thống kê học tập? Hành động này không thể hoàn tác.")) {
                  localStorage.removeItem('spt_exam_attempts');
                  window.location.reload();
                }
              }}
              className="text-xs text-slate-450 hover:text-rose-500 dark:text-slate-500 dark:hover:text-rose-400 font-semibold"
            >
              Đặt lại toàn bộ dữ liệu thống kê
            </button>
          </div>
        </>
      )}

    </div>
  );
}

export default Statistics;
