import React, { useEffect, useState } from 'react';
import reviewService from '../services/reviewService';
import { Search, BookOpen, RefreshCw, FileText, ChevronRight, X } from 'lucide-react';

export function LiteratureHub() {
  const [materials, setMaterials] = useState([]);
  const [loading, setLoading] = useState(true);
  const [search, setSearch] = useState('');
  
  // Selected material for detailed popup modal
  const [selectedMaterial, setSelectedMaterial] = useState(null);
  const [detailTab, setDetailTab] = useState('summary'); // summary, outline, values, keywords

  const loadMaterials = async () => {
    setLoading(true);
    try {
      const data = await reviewService.getLiteratureMaterials(search);
      setMaterials(data);
    } catch (err) {
      console.error("Error loading literature materials:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    loadMaterials();
  }, [search]);

  const openDetails = (material) => {
    setSelectedMaterial(material);
    setDetailTab('summary');
  };

  const closeDetails = () => {
    setSelectedMaterial(null);
  };

  return (
    <div className="space-y-6">
      {/* Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-2xl font-extrabold text-slate-800 dark:text-slate-100">Kho kiến thức Ngữ văn</h1>
          <p className="text-slate-500 dark:text-slate-400 text-sm mt-1">
            Tra cứu, ôn tập các tác phẩm Ngữ văn cốt lõi trong chương trình thi thử SPT HNUE.
          </p>
        </div>

        {/* Search */}
        <div className="relative w-full md:w-80">
          <input
            type="text"
            placeholder="Tìm tên tác phẩm, tác giả..."
            value={search}
            onChange={(e) => setSearch(e.target.value)}
            className="w-full rounded-xl border border-slate-200 dark:border-slate-700 bg-white dark:bg-slate-850 pl-10 pr-4 py-2 text-sm outline-none dark:text-slate-200"
          />
          <Search className="absolute left-3 top-2.5 w-4 h-4 text-slate-400" />
        </div>
      </div>

      {/* Materials grid */}
      {loading ? (
        <div className="flex flex-col items-center justify-center py-20 gap-2">
          <RefreshCw className="w-6 h-6 text-brand-500 animate-spin" />
          <span className="text-slate-400 text-sm">Đang tải kiến thức Ngữ văn...</span>
        </div>
      ) : materials.length === 0 ? (
        <div className="bg-white dark:bg-slate-800 rounded-2xl p-12 text-center text-slate-400 border border-slate-100 dark:border-slate-700/50">
          Không tìm thấy tác phẩm văn học nào phù hợp.
        </div>
      ) : (
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {materials.map((mat) => (
            <div 
              key={mat.id}
              onClick={() => openDetails(mat)}
              className="bg-white dark:bg-slate-800 border border-slate-100 dark:border-slate-700/50 rounded-2xl p-6 shadow-sm hover:shadow-md transition-all hover:translate-y-[-2px] cursor-pointer flex flex-col justify-between"
            >
              <div>
                <div className="flex items-center justify-between gap-4 mb-3">
                  <span className="px-2.5 py-0.5 text-xs font-bold bg-purple-50 text-purple-600 dark:bg-purple-950/40 dark:text-purple-400 rounded-full">
                    {mat.genre || 'Tác phẩm'}
                  </span>
                  <span className="text-xs text-slate-400 dark:text-slate-500">
                    {mat.epoch}
                  </span>
                </div>
                
                <h3 className="text-lg font-bold text-slate-800 dark:text-slate-100 mb-1">{mat.title}</h3>
                <p className="text-sm font-semibold text-slate-500 dark:text-slate-400 mb-3">Tác giả: {mat.author}</p>
                
                {mat.summary && (
                  <p className="text-slate-500 dark:text-slate-400 text-xs leading-relaxed line-clamp-3 mb-4">
                    {mat.summary}
                  </p>
                )}
              </div>

              <div className="flex items-center gap-1 text-xs font-bold text-brand-600 dark:text-brand-400 mt-auto pt-2 border-t border-slate-100 dark:border-slate-700/50">
                Chi tiết dàn ý & nội dung <ChevronRight className="w-3.5 h-3.5" />
              </div>
            </div>
          ))}
        </div>
      )}

      {/* Detail Modal */}
      {selectedMaterial && (
        <div className="fixed inset-0 z-50 bg-slate-900/50 backdrop-blur-sm flex items-center justify-center p-4">
          <div className="bg-white dark:bg-slate-800 w-full max-w-3xl rounded-3xl shadow-xl overflow-hidden max-h-[85vh] flex flex-col animate-scaleUp">
            
            {/* Modal Header */}
            <div className="bg-gradient-to-r from-purple-600 to-indigo-500 text-white p-6 relative">
              <button
                onClick={closeDetails}
                className="absolute right-4 top-4 p-1.5 rounded-lg bg-white/10 hover:bg-white/20 transition-colors"
              >
                <X className="w-5 h-5" />
              </button>
              <span className="text-xs font-bold bg-white/20 px-2 py-0.5 rounded-full uppercase tracking-wider">
                {selectedMaterial.genre} • {selectedMaterial.epoch}
              </span>
              <h2 className="text-2xl font-black mt-2">{selectedMaterial.title}</h2>
              <p className="text-purple-100 text-sm font-medium mt-0.5">Nhà văn / Tác giả: {selectedMaterial.author}</p>
            </div>

            {/* Modal Detail Tabs */}
            <div className="flex border-b border-slate-100 dark:border-slate-700 bg-slate-50 dark:bg-slate-900 px-6 gap-6">
              {[
                { id: 'summary', name: 'Tóm tắt' },
                { id: 'values', name: 'Giá trị nghệ thuật & nội dung' },
                { id: 'outline', name: 'Dàn ý chi tiết' },
                { id: 'keywords', name: 'Từ khóa cốt lõi' }
              ].map((t) => (
                <button
                  key={t.id}
                  onClick={() => setDetailTab(t.id)}
                  className={`py-3.5 text-xs md:text-sm font-bold border-b-2 transition-all ${
                    detailTab === t.id
                      ? 'border-purple-600 text-purple-600 dark:border-purple-400 dark:text-purple-400'
                      : 'border-transparent text-slate-500 hover:text-slate-800 dark:hover:text-slate-300'
                  }`}
                >
                  {t.name}
                </button>
              ))}
            </div>

            {/* Modal Content Scrollable Area */}
            <div className="p-6 overflow-y-auto flex-1 text-sm leading-relaxed text-slate-600 dark:text-slate-300 space-y-4">
              
              {/* Tab: Summary */}
              {detailTab === 'summary' && (
                <div className="space-y-2">
                  <h4 className="font-bold text-slate-850 dark:text-slate-100">Tóm tắt tác phẩm:</h4>
                  <p>{selectedMaterial.summary || 'Đang cập nhật...'}</p>
                </div>
              )}

              {/* Tab: Values */}
              {detailTab === 'values' && (
                <div className="space-y-4">
                  {selectedMaterial.content_value && (
                    <div>
                      <h4 className="font-bold text-purple-600 dark:text-purple-400 mb-1">Giá trị nội dung:</h4>
                      <p>{selectedMaterial.content_value}</p>
                    </div>
                  )}
                  {selectedMaterial.art_value && (
                    <div className="pt-3 border-t border-slate-100 dark:border-slate-700/50">
                      <h4 className="font-bold text-indigo-600 dark:text-indigo-400 mb-1">Giá trị nghệ thuật:</h4>
                      <p>{selectedMaterial.art_value}</p>
                    </div>
                  )}
                </div>
              )}

              {/* Tab: Outline */}
              {detailTab === 'outline' && (
                <div className="space-y-4">
                  {selectedMaterial.outline && selectedMaterial.outline.length > 0 ? (
                    <div className="space-y-3">
                      {selectedMaterial.outline.map((item, idx) => (
                        <div key={idx} className="border-l-2 border-purple-500 pl-4 py-0.5">
                          <h5 className="font-bold text-slate-800 dark:text-slate-200 text-sm mb-1">{item.section}</h5>
                          <p className="text-xs md:text-sm text-slate-500 dark:text-slate-400">{item.content}</p>
                        </div>
                      ))}
                    </div>
                  ) : (
                    <p className="text-slate-400">Chưa có thông tin dàn ý.</p>
                  )}
                </div>
              )}

              {/* Tab: Keywords */}
              {detailTab === 'keywords' && (
                <div>
                  <h4 className="font-bold text-slate-850 dark:text-slate-100 mb-3">Từ khóa ghi nhớ nhanh tác phẩm:</h4>
                  <div className="flex flex-wrap gap-2">
                    {selectedMaterial.keywords && selectedMaterial.keywords.length > 0 ? (
                      selectedMaterial.keywords.map((kw, idx) => (
                        <span 
                          key={idx}
                          className="px-3 py-1.5 rounded-xl bg-purple-55 bg-purple-50 dark:bg-purple-950/30 text-purple-700 dark:text-purple-400 font-semibold text-xs border border-purple-100/50"
                        >
                          #{kw}
                        </span>
                      ))
                    ) : (
                      <span className="text-slate-400">Chưa có từ khóa nào được thiết lập.</span>
                    )}
                  </div>
                </div>
              )}

            </div>

            {/* Modal Footer */}
            <div className="bg-slate-50 dark:bg-slate-900 border-t border-slate-100 dark:border-slate-700 p-4 flex justify-end">
              <button
                onClick={closeDetails}
                className="px-5 py-2 rounded-xl bg-slate-200 hover:bg-slate-350 dark:bg-slate-700 dark:hover:bg-slate-600 text-slate-700 dark:text-slate-200 font-bold text-xs transition-colors"
              >
                Đóng lại
              </button>
            </div>

          </div>
        </div>
      )}

    </div>
  );
}

export default LiteratureHub;
