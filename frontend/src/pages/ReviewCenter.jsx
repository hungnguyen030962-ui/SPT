import React, { useEffect, useState } from 'react';
import { useSearchParams } from 'react-router-dom';
import examService from '../services/examService';
import reviewService from '../services/reviewService';
import QuestionCard from '../components/QuestionCard';
import FlashcardComponent from '../components/FlashcardComponent';
import useLocalStorage from '../hooks/useLocalStorage';
import { 
  AlertCircle, Bookmark, RefreshCw, 
  Trash2, Award, BookOpen, Layers 
} from 'lucide-react';

export function ReviewCenter() {
  const [searchParams, setSearchParams] = useSearchParams();
  const activeTab = searchParams.get('tab') || 'wrong';

  // State from localStorage
  const [wrongIds, setWrongIds] = useLocalStorage('spt_wrong_questions', []);
  const [bookmarkIds, setBookmarkIds] = useLocalStorage('spt_bookmarks', []);
  const [learnedCardIds, setLearnedCardIds] = useLocalStorage('spt_flashcard_learned', []);

  // API loaded lists
  const [wrongQuestions, setWrongQuestions] = useState([]);
  const [bookmarkedQuestions, setBookmarkedQuestions] = useState([]);
  const [flashcards, setFlashcards] = useState([]);
  const [flashcardTopic, setFlashcardTopic] = useState('');
  
  // Loading states
  const [loadingQuestions, setLoadingQuestions] = useState(false);
  const [loadingFlashcards, setLoadingFlashcards] = useState(false);

  // States to track card answers in Review Center
  const [wrongAnswers, setWrongAnswers] = useState({});
  const [wrongShowAnswers, setWrongShowAnswers] = useState({});
  const [bookmarkAnswers, setBookmarkAnswers] = useState({});
  const [bookmarkShowAnswers, setBookmarkShowAnswers] = useState({});

  // Active flashcard study index
  const [flashcardIdx, setFlashcardIdx] = useState(0);

  // Load wrong questions
  useEffect(() => {
    if (activeTab === 'wrong' && wrongIds.length > 0) {
      const fetchWrong = async () => {
        setLoadingQuestions(true);
        try {
          const data = await examService.getQuestionsBatch(wrongIds);
          setWrongQuestions(data);
        } catch (err) {
          console.error("Error loading wrong questions:", err);
        } finally {
          setLoadingQuestions(false);
        }
      };
      fetchWrong();
    } else if (activeTab === 'wrong') {
      setWrongQuestions([]);
    }
  }, [activeTab, wrongIds]);

  // Load bookmarked questions
  useEffect(() => {
    if (activeTab === 'bookmarks' && bookmarkIds.length > 0) {
      const fetchBookmarks = async () => {
        setLoadingQuestions(true);
        try {
          const data = await examService.getQuestionsBatch(bookmarkIds);
          setBookmarkedQuestions(data);
        } catch (err) {
          console.error("Error loading bookmarked questions:", err);
        } finally {
          setLoadingQuestions(false);
        }
      };
      fetchBookmarks();
    } else if (activeTab === 'bookmarks') {
      setBookmarkedQuestions([]);
    }
  }, [activeTab, bookmarkIds]);

  // Load English flashcards
  const loadFlashcards = async () => {
    setLoadingFlashcards(true);
    try {
      const data = await reviewService.getFlashcards(flashcardTopic);
      setFlashcards(data);
      setFlashcardIdx(0);
    } catch (err) {
      console.error("Error loading flashcards:", err);
    } finally {
      setLoadingFlashcards(false);
    }
  };

  useEffect(() => {
    if (activeTab === 'flashcards') {
      loadFlashcards();
    }
  }, [activeTab, flashcardTopic]);

  // Handle re-do wrong question: If correct, remove from wrong list
  const handleSelectWrongAnswer = (qId, option, correctOption) => {
    setWrongAnswers(prev => ({ ...prev, [qId]: option }));
    setWrongShowAnswers(prev => ({ ...prev, [qId]: true }));

    if (option === correctOption) {
      // Correct! Remove from wrong IDs after a short delay so they can read explanation
      setTimeout(() => {
        setWrongIds(prev => prev.filter(id => id !== qId));
        alert("Chúc mừng! Bạn đã trả lời đúng câu sai này. Hệ thống sẽ gỡ câu này khỏi danh sách ôn tập.");
      }, 2000);
    }
  };

  const handleSelectBookmarkAnswer = (qId, option) => {
    setBookmarkAnswers(prev => ({ ...prev, [qId]: option }));
    setBookmarkShowAnswers(prev => ({ ...prev, [qId]: true }));
  };

  // Toggle bookmark (removing from list)
  const handleToggleBookmark = (qId) => {
    setBookmarkIds(prev => prev.filter(id => id !== qId));
    setBookmarkedQuestions(prev => prev.filter(q => q.id !== qId));
  };

  // Flashcards actions
  const handleMarkFlashcardLearned = (cardId) => {
    setLearnedCardIds(prev => [...prev, cardId]);
    goToNextFlashcard();
  };

  const handleMarkFlashcardReview = (cardId) => {
    // If it was marked as learned, remove from learned list
    setLearnedCardIds(prev => prev.filter(id => id !== cardId));
    goToNextFlashcard();
  };

  const goToNextFlashcard = () => {
    setFlashcardIdx(prev => (prev + 1) % activeFlashcards.length);
  };

  // Filter out learned cards from display in study session
  const activeFlashcards = flashcards.filter(c => !learnedCardIds.includes(c.id));

  // Distinct topics for flashcards
  const flashcardTopics = ["Education", "Environment", "Technology", "Psychology", "Society", "Working"];

  return (
    <div className="space-y-6">
      {/* Header */}
      <div>
        <h1 className="text-2xl font-extrabold text-slate-800 dark:text-slate-100">Trung tâm ôn tập</h1>
        <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">Củng cố kiến thức bằng cách làm lại câu làm sai, xem câu đánh dấu và học từ vựng tiếng Anh.</p>
      </div>

      {/* Tabs Row */}
      <div className="flex border-b border-slate-200 dark:border-slate-800 gap-6">
        {[
          { id: 'wrong', name: `Câu làm sai (${wrongIds.length})` },
          { id: 'bookmarks', name: `Đã đánh dấu (${bookmarkIds.length})` },
          { id: 'flashcards', name: `Từ vựng Flashcard` }
        ].map((tab) => (
          <button
            key={tab.id}
            onClick={() => setSearchParams({ tab: tab.id })}
            className={`pb-3 text-sm font-bold border-b-2 transition-all ${
              activeTab === tab.id
                ? 'border-brand-600 text-brand-600 dark:border-brand-500 dark:text-brand-400'
                : 'border-transparent text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'
            }`}
          >
            {tab.name}
          </button>
        ))}
      </div>

      {/* Tab Contents: WRONG QUESTIONS */}
      {activeTab === 'wrong' && (
        <div className="space-y-6">
          {loadingQuestions ? (
            <div className="flex flex-col items-center justify-center py-20 gap-2">
              <RefreshCw className="w-6 h-6 text-brand-500 animate-spin" />
              <span className="text-slate-400 text-sm">Đang tải câu hỏi làm sai...</span>
            </div>
          ) : wrongQuestions.length === 0 ? (
            <div className="bg-white dark:bg-slate-800 rounded-2xl p-12 border border-slate-100 dark:border-slate-700/50 text-center text-slate-400 space-y-2">
              <div className="text-4xl">🎉</div>
              <h3 className="font-bold text-slate-700 dark:text-slate-300">Không có câu hỏi sai!</h3>
              <p className="text-sm">Tuyệt vời! Bạn không có câu hỏi nào bị sai hoặc đã sửa sai hoàn tất tất cả câu hỏi.</p>
            </div>
          ) : (
            <div className="space-y-6">
              <div className="flex items-center justify-between text-xs font-semibold text-slate-400 uppercase tracking-wider">
                <span>Làm lại câu sai (Nếu giải đúng, câu đó sẽ tự động gỡ ra khỏi danh sách)</span>
                <button
                  onClick={() => {
                    if (window.confirm("Bạn có muốn xóa toàn bộ danh sách câu làm sai?")) {
                      setWrongIds([]);
                    }
                  }}
                  className="inline-flex items-center gap-1 text-rose-500 hover:text-rose-600 transition-colors"
                >
                  <Trash2 className="w-3.5 h-3.5" /> Xóa tất cả câu sai
                </button>
              </div>
              <div className="space-y-6">
                {wrongQuestions.map((q) => (
                  <QuestionCard
                    key={q.id}
                    question={q}
                    selectedAnswer={wrongAnswers[q.id]}
                    onSelectAnswer={(opt) => handleSelectWrongAnswer(q.id, opt, q.correct_answer)}
                    showAnswer={wrongShowAnswers[q.id]}
                    isBookmarked={bookmarkIds.includes(q.id)}
                    onToggleBookmark={(id) => {
                      setBookmarkIds(prev => prev.includes(id) ? prev.filter(x => x !== id) : [...prev, id]);
                    }}
                  />
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* Tab Contents: BOOKMARKS */}
      {activeTab === 'bookmarks' && (
        <div className="space-y-6">
          {loadingQuestions ? (
            <div className="flex flex-col items-center justify-center py-20 gap-2">
              <RefreshCw className="w-6 h-6 text-brand-500 animate-spin" />
              <span className="text-slate-400 text-sm">Đang tải câu hỏi đã lưu...</span>
            </div>
          ) : bookmarkedQuestions.length === 0 ? (
            <div className="bg-white dark:bg-slate-800 rounded-2xl p-12 border border-slate-100 dark:border-slate-700/50 text-center text-slate-400 space-y-1">
              <Bookmark className="w-8 h-8 mx-auto text-slate-300 dark:text-slate-600 mb-2" />
              <h3 className="font-bold text-slate-700 dark:text-slate-300">Không có câu hỏi đã lưu</h3>
              <p className="text-sm">Nhấp biểu tượng bookmark trên mỗi câu hỏi để lưu trữ ôn tập tại đây.</p>
            </div>
          ) : (
            <div className="space-y-6">
              <div className="text-xs font-semibold text-slate-400 uppercase tracking-wider">
                Danh sách các câu hỏi đã đánh dấu
              </div>
              <div className="space-y-6">
                {bookmarkedQuestions.map((q) => (
                  <QuestionCard
                    key={q.id}
                    question={q}
                    selectedAnswer={bookmarkAnswers[q.id]}
                    onSelectAnswer={(opt) => handleSelectBookmarkAnswer(q.id, opt)}
                    showAnswer={bookmarkShowAnswers[q.id]}
                    isBookmarked={true}
                    onToggleBookmark={handleToggleBookmark}
                  />
                ))}
              </div>
            </div>
          )}
        </div>
      )}

      {/* Tab Contents: ENGLISH FLASHCARDS */}
      {activeTab === 'flashcards' && (
        <div className="space-y-6 max-w-xl mx-auto">
          
          {/* Topic Select for Vocab */}
          <div className="bg-white dark:bg-slate-800 p-4 rounded-2xl border border-slate-100 dark:border-slate-700/50 flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <span className="text-sm font-bold text-slate-700 dark:text-slate-300 flex items-center gap-1.5">
              <Layers className="w-4 h-4 text-brand-500" /> Chọn chủ đề từ vựng:
            </span>
            <select
              value={flashcardTopic}
              onChange={(e) => setFlashcardTopic(e.target.value)}
              className="rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent px-3 py-1.5 text-sm outline-none dark:text-slate-200"
            >
              <option value="">Tất cả từ vựng</option>
              {flashcardTopics.map((t, idx) => (
                <option key={idx} value={t}>{t}</option>
              ))}
            </select>
          </div>

          {loadingFlashcards ? (
            <div className="flex flex-col items-center justify-center py-20 gap-2">
              <RefreshCw className="w-6 h-6 text-brand-500 animate-spin" />
              <span className="text-slate-400 text-sm">Đang tải flashcard...</span>
            </div>
          ) : activeFlashcards.length === 0 ? (
            <div className="bg-white dark:bg-slate-800 rounded-2xl p-12 border border-slate-100 dark:border-slate-700/50 text-center text-slate-400 space-y-4">
              <Award className="w-12 h-12 mx-auto text-emerald-500" />
              <div>
                <h3 className="font-bold text-slate-700 dark:text-slate-300 text-lg">Học từ vựng hoàn tất!</h3>
                <p className="text-sm mt-1">
                  Chúc mừng bạn đã học xong toàn bộ {flashcards.length} từ vựng thuộc chuyên đề này.
                </p>
              </div>
              <button
                onClick={() => setLearnedCardIds(prev => prev.filter(id => !flashcards.map(f => f.id).includes(id)))}
                className="px-5 py-2 bg-brand-600 text-white rounded-xl text-sm font-bold hover:bg-brand-700 transition-colors"
              >
                Học lại từ đầu chuyên đề này
              </button>
            </div>
          ) : (
            <div className="space-y-4">
              <div className="text-center text-xs font-bold text-slate-400 uppercase tracking-widest">
                Đang học: {flashcardIdx + 1} / {activeFlashcards.length} từ vựng chưa thuộc
              </div>
              
              {/* Flashcard Component */}
              {activeFlashcards[flashcardIdx] && (
                <FlashcardComponent
                  card={activeFlashcards[flashcardIdx]}
                  onMarkLearned={handleMarkFlashcardLearned}
                  onMarkReview={handleMarkFlashcardReview}
                />
              )}
              
              <div className="pt-2 text-center">
                <button
                  onClick={() => setLearnedCardIds([])}
                  className="text-xs text-slate-400 hover:text-slate-600 dark:hover:text-slate-300 font-semibold"
                >
                  Xóa lịch sử đã thuộc (Thiết lập lại từ đầu)
                </button>
              </div>
            </div>
          )}

        </div>
      )}

    </div>
  );
}

export default ReviewCenter;
