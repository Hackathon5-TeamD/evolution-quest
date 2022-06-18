import axios from "axios";
const Url = `http://localhost:3001`;

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
    played_at: Date.now(),
  };
  try {
    const res = await axios.post(`${Url}/result`, data);
    console.log(res);
  } catch (err) {
    console.log(err);
  }
};
