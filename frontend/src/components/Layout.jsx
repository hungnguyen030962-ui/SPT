import React, { useState } from 'react';
import { Outlet } from 'react-router-dom';
import Navbar from './Navbar';
import Sidebar from './Sidebar';

export function Layout() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(prev => !prev);
  };

  const closeSidebar = () => {
    setIsSidebarOpen(false);
  };

  return (
    <div className="min-h-screen bg-slate-50 dark:bg-slate-950 flex flex-col transition-colors duration-200">
      <Navbar onToggleSidebar={toggleSidebar} />
      
      <div className="flex flex-1 pt-16">
        <Sidebar isOpen={isSidebarOpen} onClose={closeSidebar} />
        
        {/* Main Content Area */}
        <main className="flex-1 md:pl-64 min-w-0">
          <div className="max-w-7xl mx-auto px-4 py-8 md:px-8">
            <Outlet />
          </div>
        </main>
      </div>
    </div>
  );
}

export default Layout;
