import React, { useEffect, useState } from 'react';
import examService from '../services/examService';
import QuestionCard from '../components/QuestionCard';
import useLocalStorage from '../hooks/useLocalStorage';
import { Search, Filter, RefreshCw, AlertCircle } from 'lucide-react';

export function QuestionBank() {
  const [questions, setQuestions] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Filters state
  const [subject, setSubject] = useState('');
  const [examName, setExamName] = useState('');
  const [topic, setTopic] = useState('');
  const [difficulty, setDifficulty] = useState('');
  const [search, setSearch] = useState('');
  
  // Available topics loaded from API
  const [topicsMap, setTopicsMap] = useState({});

  // Local storage for bookmarks
  const [bookmarks, setBookmarks] = useLocalStorage('spt_bookmarks', []);

  // Track answer selections in QuestionBank mode (separate from exams)
  const [userAnswers, setUserAnswers] = useState({});
  const [showAnswers, setShowAnswers] = useState({});

  useEffect(() => {
    // Load all unique topics
    const fetchTopics = async () => {
      try {
        const data = await examService.getTopics();
        setTopicsMap(data);
      } catch (err) {
        console.error("Error loading topics:", err);
      }
    };
    fetchTopics();
  }, []);

  const loadQuestions = async () => {
    setLoading(true);
    setError(null);
    try {
      const params = {};
      if (subject) params.subject = subject;
      if (examName) params.exam_name = examName;
      if (topic) params.topic = topic;
      if (difficulty) params.difficulty = difficulty;
      if (search) params.search = search;

      const data = await examService.getQuestions(params);
      setQuestions(data);
    } catch (err) {
      console.error("Error loading questions:", err);
      setError("Không thể tải danh sách câu hỏi. Vui lòng kiểm tra lại kết nối.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadQuestions();
  }, [subject, examName, topic, difficulty]);

  const handleSearchSubmit = (e) => {
    e.preventDefault();
    loadQuestions();
  };

  const handleToggleBookmark = (id) => {
    setBookmarks(prev => {
      if (prev.includes(id)) {
        return prev.filter(bId => bId !== id);
      } else {
        return [...prev, id];
      }
    });
  };

  const handleSelectAnswer = (questionId, option) => {
    setUserAnswers(prev => ({ ...prev, [questionId]: option }));
    setShowAnswers(prev => ({ ...prev, [questionId]: true }));
  };

  // Get active topics list based on selected subject
  const activeTopics = subject ? (topicsMap[subject] || []) : Object.values(topicsMap).flat();

  return (
    <div className="space-y-6">
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-800 dark:text-slate-100">Ngân hàng câu hỏi</h1>
          <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">Tra cứu, luyện tập các câu hỏi phân loại theo chuyên đề và độ khó.</p>
        </div>
      </div>

      {/* Filter panel */}
      <div className="bg-white dark:bg-slate-800 p-5 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700/50">
        <form onSubmit={handleSearchSubmit} className="space-y-4">
          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
            
            {/* Subject Select */}
            <div>
              <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-2">Môn học</label>
              <select
                value={subject}
                onChange={(e) => { setSubject(e.target.value); setTopic(''); }}
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent px-4 py-2.5 text-sm outline-none dark:text-slate-200"
              >
                <option value="" className="dark:bg-slate-800">Tất cả môn</option>
                <option value="math" className="dark:bg-slate-800">Toán học</option>
                <option value="literature" className="dark:bg-slate-800">Ngữ văn</option>
                <option value="english" className="dark:bg-slate-800">Tiếng Anh</option>
              </select>
            </div>

            {/* Topic or Exam Select */}
            {subject === 'math' ? (
              <div>
                <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-2">Đề thi (Toán)</label>
                <select
                  value={examName}
                  onChange={(e) => setExamName(e.target.value)}
                  className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent px-4 py-2.5 text-sm outline-none dark:text-slate-200"
                >
                  <option value="" className="dark:bg-slate-800">Tất cả đề thi</option>
                  {["Đề số 1", "Đề số 2", "Đề số 3", "Đề số 4", "Đề số 5", "Đề số 6"].map((name, idx) => (
                    <option key={idx} value={name} className="dark:bg-slate-800">{name}</option>
                  ))}
                </select>
              </div>
            ) : (
              <div>
                <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-2">Chuyên đề</label>
                <select
                  value={topic}
                  onChange={(e) => setTopic(e.target.value)}
                  className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent px-4 py-2.5 text-sm outline-none dark:text-slate-200"
                >
                  <option value="" className="dark:bg-slate-800">Tất cả chuyên đề</option>
                  {activeTopics.map((t, idx) => (
                    <option key={idx} value={t} className="dark:bg-slate-800">{t}</option>
                  ))}
                </select>
              </div>
            )}

            {/* Difficulty Select */}
            <div>
              <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-2">Độ khó</label>
              <select
                value={difficulty}
                onChange={(e) => setDifficulty(e.target.value)}
                className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent px-4 py-2.5 text-sm outline-none dark:text-slate-200"
              >
                <option value="" className="dark:bg-slate-800">Tất cả độ khó</option>
                <option value="easy" className="dark:bg-slate-800">Dễ</option>
                <option value="medium" className="dark:bg-slate-800">Trung bình</option>
                <option value="hard" className="dark:bg-slate-800">Khó</option>
              </select>
            </div>

            {/* Search Input */}
            <div>
              <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-2">Tìm kiếm từ khóa</label>
              <div className="relative">
                <input
                  type="text"
                  placeholder="Nội dung câu hỏi..."
                  value={search}
                  onChange={(e) => setSearch(e.target.value)}
                  className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent pl-10 pr-4 py-2.5 text-sm outline-none dark:text-slate-200"
                />
                <Search className="absolute left-3.5 top-3 w-4 h-4 text-slate-400" />
              </div>
            </div>

          </div>

          <div className="flex items-center justify-between border-t border-slate-100 dark:border-slate-700/50 pt-4">
            <button
              type="button"
              onClick={() => {
                setSubject('');
                setExamName('');
                setTopic('');
                setDifficulty('');
                setSearch('');
              }}
              className="text-xs font-bold text-slate-400 hover:text-slate-600 dark:hover:text-slate-300"
            >
              Đặt lại bộ lọc
            </button>
            <button
              type="submit"
              className="px-5 py-2 rounded-xl bg-brand-600 hover:bg-brand-700 text-white font-semibold text-sm shadow-md transition-colors"
            >
              Tìm kiếm
            </button>
          </div>
        </form>
      </div>

      {/* Questions list */}
      {loading ? (
        <div className="flex flex-col items-center justify-center py-20 gap-3">
          <RefreshCw className="w-8 h-8 text-brand-500 animate-spin" />
          <span className="text-slate-400 text-sm">Đang tìm kiếm câu hỏi...</span>
        </div>
      ) : error ? (
        <div className="flex flex-col items-center justify-center py-16 text-rose-500 gap-2">
          <AlertCircle className="w-8 h-8" />
          <span className="font-semibold">{error}</span>
        </div>
      ) : questions.length === 0 ? (
        <div className="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700/50 rounded-2xl p-12 text-center text-slate-400">
          Không tìm thấy câu hỏi nào phù hợp với bộ lọc đã chọn.
        </div>
      ) : (
        <div className="space-y-6">
          <div className="text-sm font-semibold text-slate-400 uppercase tracking-wider">
            Kết quả: Tìm thấy {questions.length} câu hỏi
          </div>
          <div className="space-y-6">
            {questions.map((q) => (
              <QuestionCard
                key={q.id}
                question={q}
                selectedAnswer={userAnswers[q.id]}
                onSelectAnswer={(opt) => handleSelectAnswer(q.id, opt)}
                showAnswer={showAnswers[q.id]}
                isBookmarked={bookmarks.includes(q.id)}
                onToggleBookmark={handleToggleBookmark}
              />
            ))}
          </div>
        </div>
      )}
    </div>
  );
}

export default QuestionBank;
