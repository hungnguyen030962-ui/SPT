import React from 'react';
import MathRenderer from './MathRenderer';
import { Bookmark, CheckCircle, XCircle } from 'lucide-react';

export function QuestionCard({
  question,
  selectedAnswer,
  onSelectAnswer,
  showAnswer = false,
  isBookmarked = false,
  onToggleBookmark,
}) {
  const options = question.options || [];

  // Helper to extract option prefix (A, B, C, D)
  const getOptionLabel = (index) => {
    return String.fromCharCode(65 + index); // 65 is 'A'
  };

  const getOptionText = (optionStr) => {
    // If option string starts with "A. ", "B. ", etc., we keep it or clean it
    return optionStr;
  };

  return (
    <div className="bg-white dark:bg-slate-800 rounded-2xl shadow-sm border border-slate-100 dark:border-slate-700/50 p-6 transition-all hover:shadow-md">
      {/* Header: Topic, Difficulty, Bookmark */}
      <div className="flex items-center justify-between gap-4 mb-4 border-b border-slate-100 dark:border-slate-700/50 pb-3">
        <div className="flex items-center gap-2">
          <span className="px-3 py-1 text-xs font-semibold rounded-full bg-brand-50 text-brand-600 dark:bg-brand-950/50 dark:text-brand-400">
            {question.topic}
          </span>
          <span className={`px-3 py-1 text-xs font-semibold rounded-full ${
            question.difficulty === 'easy'
              ? 'bg-emerald-50 text-emerald-600 dark:bg-emerald-950/30 dark:text-emerald-400'
              : question.difficulty === 'medium'
              ? 'bg-amber-50 text-amber-600 dark:bg-amber-950/30 dark:text-amber-400'
              : 'bg-rose-50 text-rose-600 dark:bg-rose-950/30 dark:text-rose-400'
          }`}>
            {question.difficulty === 'easy' ? 'Dễ' : question.difficulty === 'medium' ? 'Trung bình' : 'Khó'}
          </span>
        </div>
        
        {onToggleBookmark && (
          <button
            onClick={() => onToggleBookmark(question.id)}
            className="text-slate-400 hover:text-brand-600 dark:hover:text-brand-400 transition-colors p-1.5 rounded-lg hover:bg-slate-50 dark:hover:bg-slate-700"
            title={isBookmarked ? "Bỏ lưu câu hỏi" : "Lưu câu hỏi"}
          >
            <Bookmark className={`w-5 h-5 ${isBookmarked ? 'fill-brand-500 text-brand-500' : ''}`} />
          </button>
        )}
      </div>

      {/* Reading Passage if any */}
      {question.passage && (
        <div className="mb-4 p-4 rounded-xl bg-slate-50 dark:bg-slate-900 border border-slate-100 dark:border-slate-800 text-sm leading-relaxed max-h-60 overflow-y-auto">
          <div className="font-semibold mb-1 text-xs text-slate-400 dark:text-slate-500 uppercase tracking-wider">Ngữ liệu / Đoạn văn:</div>
          <MathRenderer text={question.passage} />
        </div>
      )}

      {/* Question Content */}
      <div className="text-base font-medium text-slate-800 dark:text-slate-100 mb-6">
        <MathRenderer text={question.content} />
      </div>

      {/* Options List / Short Answer Input */}
      {options.length === 0 ? (
        <div className="space-y-2 mb-6">
          <label className="block text-xs font-semibold text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-2">
            Nhập câu trả lời ngắn (chỉ điền số hoặc phân số):
          </label>
          <input
            type="text"
            disabled={showAnswer}
            placeholder="Nhập kết quả..."
            value={selectedAnswer || ''}
            onChange={(e) => onSelectAnswer && onSelectAnswer(e.target.value)}
            className="w-full max-w-md rounded-xl border border-slate-200 dark:border-slate-700 bg-transparent px-4 py-2.5 text-sm outline-none dark:text-slate-200 focus:border-brand-500 focus:ring-2 focus:ring-brand-500/20"
          />
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-3 mb-6">
          {options.map((option, index) => {
            const optionLabel = getOptionLabel(index); // A, B, C, D
            const isSelected = selectedAnswer === optionLabel;

            // Post-submit styling helper
            let optionStyle = "border-slate-200 dark:border-slate-700 hover:bg-slate-50 dark:hover:bg-slate-700/50";
            if (isSelected) {
              optionStyle = "border-brand-500 bg-brand-50/50 text-brand-900 dark:border-brand-500 dark:bg-brand-950/20 dark:text-brand-400";
            }

            if (showAnswer) {
              const isCorrectOption = optionLabel === question.correct_answer;
              if (isCorrectOption) {
                optionStyle = "border-emerald-500 bg-emerald-50/30 text-emerald-950 dark:border-emerald-500 dark:bg-emerald-950/20 dark:text-emerald-400 font-medium";
              } else if (isSelected) {
                optionStyle = "border-rose-500 bg-rose-50/30 text-rose-950 dark:border-rose-500 dark:bg-rose-950/20 dark:text-rose-400";
              } else {
                optionStyle = "border-slate-200 dark:border-slate-800 opacity-60";
              }
            }

            return (
              <button
                key={index}
                disabled={showAnswer}
                onClick={() => onSelectAnswer && onSelectAnswer(optionLabel)}
                className={`flex items-start gap-3 p-4 rounded-xl border text-left transition-all ${optionStyle}`}
              >
                <span className={`flex items-center justify-center w-6 h-6 rounded-full text-xs font-bold ${
                  isSelected 
                    ? 'bg-brand-600 text-white dark:bg-brand-500' 
                    : showAnswer && optionLabel === question.correct_answer
                    ? 'bg-emerald-600 text-white'
                    : showAnswer && isSelected
                    ? 'bg-rose-600 text-white'
                    : 'bg-slate-100 dark:bg-slate-700 text-slate-600 dark:text-slate-300'
                }`}>
                  {optionLabel}
                </span>
                <div className="flex-1 text-sm pt-0.5">
                  <MathRenderer text={getOptionText(option)} />
                </div>
              </button>
            );
          })}
        </div>
      )}

      {/* Answer Verification Status */}
      {showAnswer && (
        <div className="mt-4 pt-4 border-t border-slate-100 dark:border-slate-700/50">
          <div className="flex items-center gap-2 mb-3">
            {selectedAnswer?.trim().toUpperCase() === question.correct_answer?.trim().toUpperCase() ? (
              <span className="flex items-center gap-1.5 text-sm font-semibold text-emerald-600 dark:text-emerald-400">
                <CheckCircle className="w-5 h-5" /> Chính xác
              </span>
            ) : (
              <span className="flex items-center gap-1.5 text-sm font-semibold text-rose-600 dark:text-rose-400">
                <XCircle className="w-5 h-5" /> Chưa chính xác {selectedAnswer ? `(Bạn chọn: ${selectedAnswer})` : '(Bạn chưa trả lời)'}
              </span>
            )}
            <span className="text-sm text-slate-500 dark:text-slate-400 ml-auto">
              Đáp án đúng: <strong className="text-emerald-600 dark:text-emerald-400">{question.correct_answer}</strong>
            </span>
          </div>

          {/* Explanation */}
          {question.explanation && (
            <div className="bg-slate-50 dark:bg-slate-900 rounded-xl p-4 mb-3 text-sm">
              <strong className="text-slate-700 dark:text-slate-300 block mb-1">Lời giải chi tiết:</strong>
              <MathRenderer text={question.explanation} />
            </div>
          )}

          {/* Math Section: Step by step & formulas */}
          {question.subject === 'math' && (
            <div className="space-y-3">
              {question.step_by_step && question.step_by_step.length > 0 && (
                <div className="bg-blue-50/30 dark:bg-brand-950/10 rounded-xl p-4 text-sm border border-blue-100/30">
                  <strong className="text-brand-800 dark:text-brand-400 block mb-2">Lời giải từng bước:</strong>
                  <ol className="space-y-2 list-decimal list-inside">
                    {question.step_by_step.map((step, idx) => (
                      <li key={idx} className="text-slate-600 dark:text-slate-300">
                        <span className="font-semibold text-slate-800 dark:text-slate-200">{step.step}: </span>
                        <MathRenderer text={step.detail} className="inline-block" />
                      </li>
                    ))}
                  </ol>
                </div>
              )}

              {question.formulas && question.formulas.length > 0 && (
                <div className="bg-amber-50/20 dark:bg-amber-950/10 rounded-xl p-4 text-sm border border-amber-100/20">
                  <strong className="text-amber-800 dark:text-amber-400 block mb-1">Công thức liên quan:</strong>
                  <div className="flex flex-wrap gap-2 mt-1">
                    {question.formulas.map((formula, idx) => (
                      <div key={idx} className="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700 px-3 py-1.5 rounded-lg">
                        <MathRenderer text={formula} />
                      </div>
                    ))}
                  </div>
                </div>
              )}
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default QuestionCard;
