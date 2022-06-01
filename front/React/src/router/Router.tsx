import React from "react";
import { Route, Routes } from "react-router-dom";
import { Login } from "../components/Login";

export const Router = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
      </Routes>
    </>
  );
};
