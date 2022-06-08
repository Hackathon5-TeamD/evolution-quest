import axios from "axios";
const Url = `https://localhost:3001`;

export const getRanking = async (page: number) => {
  try {
    const res = await axios.get(`${Url}/result/${page}`);
    return res.data;
  } catch (err) {
    console.log(err);
  }
};
