import axios from 'axios';

const axiosInstance = axios.create({
  baseURL: 'http://127.0.0.1:5000'  // usato in locale
  //baseURL: 'http://localhost:5000' // usato con Docker
});

export default axiosInstance;
