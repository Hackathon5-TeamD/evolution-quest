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

export const getUserRecord = async (user_id: number) => {
  try {
    const res = await axios.get(`${Url}/result`, {
      // 本番用は/recordに変更する事。これはjson-serverでのやり取りのため、resultにしてる。
      // params以下は、/result/user_idとなる。
      // UserPage.tsxのgetUserRecordの引数に指定したidがここへ入る。
      params: {
        user_id: user_id,
      },
    });
    return res.data;
  } catch (err) {
    console.log(err);
  }
};
