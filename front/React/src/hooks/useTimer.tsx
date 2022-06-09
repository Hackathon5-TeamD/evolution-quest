import { useState, useEffect } from "react";

export const useTimer = () => {
  const [second, setSecond] = useState(0);
  const [min, setMin] = useState(0);
  const [isRunning, setRunning] = useState(true);

  const startTime = Date.now();

  useEffect(() => {
    if (isRunning) {
      const id = setInterval(() => {
        // const second = Math.round((Date.now() - startTime) / 1000);

        if (second >= 59) {
          setSecond((prev) => prev - 59);
          setMin((prev) => prev + 1);
        } else {
          setSecond(second + 1);
        }
      }, 1000);

      return () => clearInterval(id);
    }
  }, [isRunning, second]);

  // return { time: <p></p> };
  return { time: `${min} : ${second}` };
};
