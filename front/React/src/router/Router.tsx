import React from "react";
import { Route, Routes } from "react-router-dom";
import { Login } from "../components/Login";
import { Register } from "../components/pages/Register/Register";

export const Router = () => {
  return (
    <>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="register" element={<Register />} />
      </Routes>
    </>
  );
};
