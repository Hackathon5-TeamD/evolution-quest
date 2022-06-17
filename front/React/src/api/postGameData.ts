import axios from "axios";
// const Url = `http://localhost:3001`;
const Url = `http://localhost:5001`;

export const postGameData = async (result: {
  accuracy: number;
  wpm: number;
}) => {
  const { accuracy, wpm } = result;
  const data = {
    "accuracy_value": accuracy,
    "wpm": wpm,
    "played_at": Date.now(),
  };
  try {
    const res = await axios.post(`${Url}/result`, data);
    console.log(res);
  } catch (err) {
    console.log(err);
  }
};
