import React, { useEffect, useState } from 'react';
import { Timer } from 'lucide-react';

export function CountdownTimer({ initialSeconds, onTimeUp, isActive = true }) {
  const [secondsLeft, setSecondsLeft] = useState(initialSeconds);

  useEffect(() => {
    setSecondsLeft(initialSeconds);
  }, [initialSeconds]);

  useEffect(() => {
    if (!isActive) return;
    if (secondsLeft <= 0) {
      if (onTimeUp) onTimeUp();
      return;
    }

    const interval = setInterval(() => {
      setSecondsLeft(prev => prev - 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [secondsLeft, isActive, onTimeUp]);

  const formatTime = (totalSeconds) => {
    const mins = Math.floor(totalSeconds / 60);
    const secs = totalSeconds % 60;
    return `${mins.toString().padStart(2, '0')}:${secs.toString().padStart(2, '0')}`;
  };

  const isLowTime = secondsLeft < 60;

  return (
    <div className={`flex items-center gap-2 px-4 py-2 rounded-xl border text-sm font-bold transition-all ${
      isLowTime
        ? 'bg-rose-50 border-rose-200 text-rose-600 animate-pulse dark:bg-rose-950/20 dark:border-rose-800'
        : 'bg-slate-50 border-slate-200 text-slate-700 dark:bg-slate-800 dark:border-slate-700 dark:text-slate-200'
    }`}>
      <Timer className={`w-4 h-4 ${isLowTime ? 'text-rose-500' : 'text-slate-400 dark:text-slate-500'}`} />
      <span>{formatTime(secondsLeft)}</span>
    </div>
  );
}

export default CountdownTimer;
