import React from 'react';
import { NavLink } from 'react-router-dom';
import { 
  Home, BookOpen, FileSpreadsheet, 
  RefreshCw, FileText, BarChart3, GraduationCap 
} from 'lucide-react';

export function Sidebar({ isOpen, onClose }) {
  const menuItems = [
    { name: 'Bảng điều khiển', path: '/', icon: Home },
    { name: 'Luyện thi & Đề thi', path: '/exam', icon: FileSpreadsheet },
    { name: 'Trung tâm ôn tập', path: '/review', icon: RefreshCw },
  ];

  const sidebarClass = `fixed inset-y-0 left-0 z-50 w-64 border-r border-slate-200 bg-white pt-16 transition-transform dark:border-slate-800 dark:bg-slate-900 md:translate-x-0 ${
    isOpen ? 'translate-x-0' : '-translate-x-full'
  }`;

  return (
    <>
      {/* Mobile Sidebar Overlay */}
      {isOpen && (
        <div
          onClick={onClose}
          className="fixed inset-0 z-40 bg-slate-900/40 backdrop-blur-sm md:hidden"
        />
      )}

      <aside className={sidebarClass}>
        <div className="flex h-full flex-col justify-between overflow-y-auto px-4 py-6">
          <nav className="space-y-1.5">
            {menuItems.map((item) => (
              <NavLink
                key={item.path}
                to={item.path}
                onClick={onClose}
                className={({ isActive }) =>
                  `flex items-center gap-3 px-4 py-3 text-sm font-semibold rounded-xl transition-all ${
                    isActive
                      ? 'bg-brand-600 text-white shadow-md shadow-brand-600/10 dark:bg-brand-600'
                      : 'text-slate-600 hover:bg-slate-50 hover:text-slate-900 dark:text-slate-400 dark:hover:bg-slate-800 dark:hover:text-slate-200'
                  }`
                }
              >
                <item.icon className="w-5 h-5 flex-shrink-0" />
                <span>{item.name}</span>
              </NavLink>
            ))}
          </nav>
          
          {/* Quick info footer */}
          <div className="border-t border-slate-100 dark:border-slate-800 pt-4 mt-6">
            <div className="rounded-xl bg-slate-50 dark:bg-slate-800/50 p-4 text-xs">
              <p className="font-semibold text-slate-700 dark:text-slate-300">Tuyển sinh SPT HNUE</p>
              <p className="text-slate-400 dark:text-slate-500 mt-0.5">Luyện thi Đánh giá năng lực 3 môn Toán, Văn, Anh.</p>
            </div>
          </div>
        </div>
      </aside>
    </>
  );
}

export default Sidebar;
