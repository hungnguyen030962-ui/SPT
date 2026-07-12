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
        
        {/* Step 1: Subject Selection */}
        <div className="space-y-3">
          <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
            Bước 1: Chọn môn học
          </label>
          <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
            {[
              { id: 'math', name: 'Toán học', desc: 'Lời giải chi tiết & công thức', color: 'border-blue-500/20 text-blue-600 bg-blue-50/20' },
              { id: 'literature', name: 'Ngữ văn', desc: 'Đọc hiểu & kiến thức chung', color: 'border-purple-500/20 text-purple-600 bg-purple-50/20' },
              { id: 'english', name: 'Tiếng Anh', desc: 'Ngữ pháp, từ vựng, đọc hiểu', color: 'border-amber-500/20 text-amber-600 bg-amber-50/20' }
            ].map((sub) => {
              const isSelected = subject === sub.id;
              return (
                <button
                  key={sub.id}
                  onClick={() => {
                    setSubject(sub.id);
                    setTopic('');
                  }}
                  className={`flex flex-col items-start p-4 rounded-2xl border text-left transition-all ${
                    isSelected
                      ? 'border-brand-600 bg-brand-50/30 text-slate-800 dark:border-brand-500 dark:bg-brand-950/20 dark:text-slate-100 ring-2 ring-brand-600/10'
                      : 'border-slate-200 hover:bg-slate-50 dark:border-slate-700 dark:hover:bg-slate-700/30 text-slate-700 dark:text-slate-300'
                  }`}
                >
                  <span className="font-bold text-base mb-1">{sub.name}</span>
                  <span className="text-xs text-slate-400 dark:text-slate-500">{sub.desc}</span>
                </button>
              );
            })}
          </div>
        </div>

        {/* Step 2: Exam Mode Selection */}
        {subject === 'math' ? (
          <div className="space-y-3">
            <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
              Bước 2: Chọn đề thi môn Toán (HNUE)
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
                    <span className="text-xs text-slate-400 dark:text-slate-500 mt-0.5">90 phút • Trắc nghiệm</span>
                  </button>
                );
              })}
            </div>
          </div>
        ) : (
          <>
            <div className="space-y-3">
              <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                Bước 2: Chọn hình thức thi
              </label>
              <div className="grid grid-cols-1 sm:grid-cols-3 gap-3">
                {[
                  { id: 'random', name: 'Luyện ngẫu nhiên', icon: Sparkles, desc: 'Câu hỏi ngẫu nhiên' },
                  { id: 'topic', name: 'Luyện theo chuyên đề', icon: Layers, desc: 'Chọn chuyên đề cụ thể' },
                  { id: 'full', name: 'Đề tổng hợp', icon: BookOpen, desc: 'Đầy đủ nội dung thi' }
                ].map((mode) => {
                  const isSelected = examType === mode.id;
                  return (
                    <button
                      key={mode.id}
                      type="button"
                      onClick={() => setExamType(mode.id)}
                      className={`flex flex-col items-center justify-center p-5 rounded-2xl border text-center transition-all ${
                        isSelected
                          ? 'border-brand-600 bg-brand-50/30 text-brand-700 dark:border-brand-500 dark:bg-brand-950/20 dark:text-brand-400 ring-2 ring-brand-600/10'
                          : 'border-slate-200 hover:bg-slate-50 dark:border-slate-700 dark:hover:bg-slate-700/30 text-slate-700 dark:text-slate-300'
                      }`}
                    >
                      <mode.icon className="w-5 h-5 mb-2 text-brand-500" />
                      <span className="font-bold text-sm mb-0.5">{mode.name}</span>
                      <span className="text-xs text-slate-400 dark:text-slate-500">{mode.desc}</span>
                    </button>
                  );
                })}
              </div>
            </div>

            {/* Conditional Field: Topic Selector */}
            {examType === 'topic' && (
              <div className="space-y-2 animate-fadeIn">
                <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                  Chọn chuyên đề cụ thể
                </label>
                <select
                  value={topic}
                  onChange={(e) => setTopic(e.target.value)}
                  className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent px-4 py-2.5 text-sm outline-none dark:text-slate-200"
                >
                  <option value="">-- Vui lòng chọn chuyên đề --</option>
                  {activeTopics.map((t, idx) => (
                    <option key={idx} value={t}>{t}</option>
                  ))}
                </select>
                {activeTopics.length === 0 && !loadingTopics && (
                  <p className="text-xs text-amber-500">Môn học này hiện chưa có chuyên đề nào được nạp dữ liệu câu hỏi.</p>
                )}
              </div>
            )}
          </>
        )}

        {/* Step 3: Limits & Timers */}
        {subject === 'math' ? (
          <div className="p-5 rounded-2xl bg-blue-50/30 dark:bg-slate-900/30 border border-blue-100/30 dark:border-slate-700/50 text-sm text-slate-600 dark:text-slate-400">
            <span className="font-bold text-brand-700 dark:text-brand-400 block mb-1">Thông tin đề thi thử môn Toán:</span>
            Thời gian làm bài là **90 phút**. Đề thi gồm các câu hỏi trắc nghiệm chuẩn cấu trúc tuyển sinh Đại học Sư phạm Hà Nội. Kết quả và bảng điểm chi tiết kèm lời giải từng bước sẽ được hiển thị ngay sau khi nộp bài.
          </div>
        ) : (
          <div className="grid grid-cols-1 sm:grid-cols-2 gap-6 pt-2">
            {/* Question Limit */}
            <div className="space-y-3">
              <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                Số lượng câu hỏi
              </label>
              <div className="flex gap-2">
                {[5, 10, 15, 20].map((num) => (
                  <button
                    key={num}
                    type="button"
                    onClick={() => setLimit(num)}
                    className={`flex-1 py-2 text-sm font-bold rounded-xl border transition-all ${
                      limit === num
                        ? 'bg-slate-900 border-slate-900 text-white dark:bg-slate-100 dark:border-slate-100 dark:text-slate-900'
                        : 'border-slate-200 hover:bg-slate-50 dark:border-slate-700 dark:hover:bg-slate-700'
                    }`}
                  >
                    {num} câu
                  </button>
                ))}
              </div>
            </div>

            {/* Time Limit */}
            <div className="space-y-3">
              <label className="flex items-center justify-between text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider">
                <span>Thời gian làm bài</span>
                <span className="text-brand-600 dark:text-brand-400 lowercase font-normal">{timeLimit} phút</span>
              </label>
              <div className="flex items-center gap-3">
                <Clock className="w-4 h-4 text-slate-400 shrink-0" />
                <input
                  type="range"
                  min="5"
                  max="60"
                  step="5"
                  value={timeLimit}
                  onChange={(e) => setTimeLimit(parseInt(e.target.value))}
                  className="w-full h-1 bg-slate-200 dark:bg-slate-700 rounded-lg appearance-none cursor-pointer accent-brand-600"
                />
              </div>
            </div>
          </div>
        )}

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
