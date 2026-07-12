import api from './api';

export const reviewService = {
  getLiteratureMaterials: async (search = '') => {
    const response = await api.get('/literature/materials', {
      params: search ? { search } : {},
    });
    return response.data;
  },

  getLiteratureMaterialById: async (id) => {
    const response = await api.get(`/literature/materials/${id}`);
    return response.data;
  },

  getFlashcards: async (topic = '') => {
    const response = await api.get('/flashcards/', {
      params: topic ? { topic } : {},
    });
    return response.data;
  },

  getRandomFlashcards: async (limit = 10) => {
    const response = await api.get('/flashcards/random', {
      params: { limit },
    });
    return response.data;
  },
};

export default reviewService;
