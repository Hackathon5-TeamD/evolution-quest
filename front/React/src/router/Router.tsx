import React from "react";
import { Route, Routes } from "react-router-dom";
import { Login } from "../components/Login";
import { MainPage } from "../components/pages/Main/MainPage";
import { Register } from "../components/pages/Register/Register";
import { ResultRank } from "../components/pages/Result/ResultRank";
import { GameStart } from "../components/pages/Start/GameStart";
import { UserPage } from "../components/pages/User/UserPage";

export const Router = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="register" element={<Register />} />
        <Route path="gamestart" element={<GameStart />} />
        <Route path="userpage" element={<UserPage />} />
        <Route path="main" element={<MainPage />} />
        <Route path="result" element={<ResultRank />} />
      </Routes>
    </>
  );
};