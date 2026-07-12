import React, { useState } from 'react';
import { RefreshCw, Check, X } from 'lucide-react';

export function FlashcardComponent({ card, onMarkLearned, onMarkReview }) {
  const [isFlipped, setIsFlipped] = useState(false);

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  return (
    <div className="flex flex-col items-center max-w-sm w-full mx-auto">
      {/* 3D Flip Card Container */}
      <div 
        onClick={handleFlip}
        className={`flip-card w-full h-64 cursor-pointer relative ${isFlipped ? 'flipped' : ''}`}
      >
        <div className="flip-card-inner w-full h-full relative duration-500 transform-style-3d">
          
          {/* Front Side: Word, Pronunciation, Part of Speech */}
          <div className="flip-card-front absolute inset-0 w-full h-full bg-gradient-to-br from-brand-500 to-brand-600 rounded-2xl shadow-lg flex flex-col justify-between p-6 text-white overflow-hidden">
            {/* Glossy background circle */}
            <div className="absolute -right-16 -top-16 w-40 h-40 bg-white/10 rounded-full blur-xl" />
            
            <div className="flex items-center justify-between z-10">
              <span className="text-xs font-semibold px-2 py-0.5 bg-white/20 rounded-full tracking-wider uppercase">
                {card.part_of_speech || 'Từ vựng'}
              </span>
              <span className="text-xs text-brand-100 flex items-center gap-1">
                <RefreshCw className="w-3.5 h-3.5" /> Click để lật
              </span>
            </div>

            <div className="text-center my-auto z-10">
              <h2 className="text-3xl font-extrabold tracking-tight mb-2">{card.word}</h2>
              {card.ipa && <p className="text-brand-100 font-mono text-base">{card.ipa}</p>}
            </div>

            <div className="text-center text-xs text-brand-200 z-10">
              Chủ đề: {card.topic || 'Chung'}
            </div>
          </div>

          {/* Back Side: Translation, Example */}
          <div className="flip-card-back absolute inset-0 w-full h-full bg-white dark:bg-slate-800 rounded-2xl shadow-lg border border-slate-100 dark:border-slate-700/50 flex flex-col justify-between p-6 overflow-hidden">
            <div className="flex items-center justify-between text-xs text-slate-400 dark:text-slate-500">
              <span>Định nghĩa & Nghĩa</span>
              <span className="flex items-center gap-1">
                <RefreshCw className="w-3.5 h-3.5" /> Click để lật
              </span>
            </div>

            <div className="my-auto text-center space-y-4">
              <div>
                <p className="text-xs text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-1">Nghĩa tiếng Việt</p>
                <h3 className="text-xl font-bold text-slate-800 dark:text-slate-100">{card.meaning}</h3>
              </div>
              
              {card.example && (
                <div className="pt-2 border-t border-slate-100 dark:border-slate-700/50">
                  <p className="text-xs text-slate-400 dark:text-slate-500 uppercase tracking-wider mb-1">Ví dụ minh họa</p>
                  <p className="text-sm italic text-slate-600 dark:text-slate-300 font-medium">"{card.example}"</p>
                </div>
              )}
            </div>

            <div className="text-center text-xs text-slate-400 dark:text-slate-500">
              Chủ đề: {card.topic || 'Chung'}
            </div>
          </div>

        </div>
      </div>

      {/* Action Buttons */}
      <div className="flex items-center justify-center gap-4 mt-6 w-full">
        <button
          onClick={(e) => {
            e.stopPropagation();
            setIsFlipped(false);
            onMarkReview(card.id);
          }}
          className="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl border border-slate-200 dark:border-slate-700 text-slate-700 dark:text-slate-300 bg-white dark:bg-slate-800 hover:bg-slate-50 dark:hover:bg-slate-700 text-sm font-semibold transition-colors"
        >
          <X className="w-4 h-4 text-rose-500" /> Chưa thuộc
        </button>
        <button
          onClick={(e) => {
            e.stopPropagation();
            setIsFlipped(false);
            onMarkLearned(card.id);
          }}
          className="flex-1 flex items-center justify-center gap-2 px-4 py-2.5 rounded-xl bg-emerald-600 text-white hover:bg-emerald-700 text-sm font-semibold transition-colors shadow-md shadow-emerald-600/10"
        >
          <Check className="w-4 h-4" /> Đã thuộc
        </button>
      </div>
    </div>
  );
}

export default FlashcardComponent;
