import axios from "axios";

const API_URL = "http://localhost:5432/api/";

export default {
  async getProducts() {
    const response = await axios.get(`${API_URL}products/`);
    return response.data;
  },
};
