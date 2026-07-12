import React from 'react';
import { useTheme } from '../context/ThemeContext';
import { Sun, Moon, Menu, GraduationCap } from 'lucide-react';
import { Link } from 'react-router-dom';

export function Navbar({ onToggleSidebar }) {
  const { isDark, toggleTheme } = useTheme();

  return (
    <header className="sticky top-0 z-40 w-full border-b border-slate-200 bg-white/80 dark:border-slate-800 dark:bg-slate-900/80 backdrop-blur-md">
      <div className="flex h-16 items-center justify-between px-6">
        
        {/* Left Side: Mobile Menu Button & Brand */}
        <div className="flex items-center gap-4">
          <button
            onClick={onToggleSidebar}
            className="rounded-lg p-2 text-slate-500 hover:bg-slate-100 focus:outline-none dark:text-slate-400 dark:hover:bg-slate-800 md:hidden"
            aria-label="Toggle sidebar"
          >
            <Menu className="w-5 h-5" />
          </button>
          
          <Link to="/" className="flex items-center gap-2.5">
            <div className="flex h-9 w-9 items-center justify-center rounded-xl bg-brand-600 text-white shadow-md shadow-brand-600/20">
              <GraduationCap className="w-5 h-5" />
            </div>
            <span className="font-extrabold text-lg tracking-tight bg-gradient-to-r from-brand-600 to-blue-500 bg-clip-text text-transparent dark:from-brand-400 dark:to-blue-400">
              SPT HNUE Prep
            </span>
          </Link>
        </div>

        {/* Right Side: Theme Toggle & Info */}
        <div className="flex items-center gap-3">
          <button
            onClick={toggleTheme}
            className="rounded-xl border border-slate-200 p-2.5 text-slate-500 hover:bg-slate-50 dark:border-slate-800 dark:text-slate-400 dark:hover:bg-slate-800 transition-colors"
            title={isDark ? "Chuyển sang giao diện sáng" : "Chuyển sang giao diện tối"}
          >
            {isDark ? <Sun className="w-4 h-4 text-amber-500" /> : <Moon className="w-4 h-4" />}
          </button>
          
          <span className="hidden sm:inline-block px-3 py-1 text-xs font-semibold rounded-full bg-slate-100 text-slate-600 dark:bg-slate-800 dark:text-slate-400">
            Học viên Tự do
          </span>
        </div>

      </div>
    </header>
  );
}

export default Navbar;
