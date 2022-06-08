import axios from "axios";
const Url = `http://localhost:3001`;

export const getRanking = async (page: number) => {
  try {
    console.log(`${Url}/results/${page}`);

    const res = await axios.get(`${Url}/results/${page}`);
    return res.data;
  } catch (err) {
    console.log(err);
  }
};
