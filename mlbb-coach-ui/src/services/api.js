import axios from "axios";

const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000";

export async function generateGuide(data) {
  try {
    const response = await axios.post(`${API_URL}/generate-guide`, data);

    return response.data;
  } catch (error) {
    console.error("Backend connection error:", error);

    throw error;
  }
}
