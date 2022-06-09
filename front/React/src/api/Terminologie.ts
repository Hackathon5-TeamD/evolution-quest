import axios from "axios";
const Url = `http://localhost:3001`;

export const getTerminologie = async () => {
  try {
    const res = await axios.get(`${Url}/terminologie`);
    console.log(res.data);
    return res.data;
  } catch (err) {
    console.log(err);
  }
};
