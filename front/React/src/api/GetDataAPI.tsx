import axios from "axios";
const Url = `http://localhost:3001`;

export const getRanking = async (page: number) => {
  try {
    const res = await axios.get(`${Url}/results/${page}`);
    return res.data;
  } catch (err) {
    console.log(err);
  }
};

export const getUserRecord = async () => {
  try {
    const res = await axios.get(`${Url}/record`);
    return res.data;
  } catch (err) {
    console.log(err);
  }
};
