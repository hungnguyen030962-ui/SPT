import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { ThemeProvider } from './context/ThemeContext';
import Layout from './components/Layout';
import Home from './pages/Home';
import ExamLobby from './pages/ExamLobby';
import ExamActive from './pages/ExamActive';
import ExamResult from './pages/ExamResult';
import ReviewCenter from './pages/ReviewCenter';

export function App() {
  return (
    <ThemeProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Layout />}>
            <Route index element={<Home />} />
            <Route path="exam" element={<ExamLobby />} />
            <Route path="exam/active" element={<ExamActive />} />
            <Route path="exam/result" element={<ExamResult />} />
            <Route path="review" element={<ReviewCenter />} />
          </Route>
        </Routes>
      </BrowserRouter>
    </ThemeProvider>
  );
}

export default App;

