import axios from "axios";
// const Url = `http://localhost:3001`;
// const Url = `http://192.168.0.102:5000`;
// const Url = `http://127.0.0.1:5000`;
const Url = `http://localhost:5000`;

export const postGameData = async (result: {
  user_id: number;
  accuracy: number;
  wpm: number;
}) => {
  const { accuracy, wpm, user_id } = result;
  const data = {
    user_id: user_id,
    accuracy_value: accuracy,
    wpm: wpm,
    played_at_date: Date.now(),
  };
  try {
    const res = await axios.post(`${Url}/result`, data);
    console.log(res);
  } catch (err) {
    console.log(err);
  }
};