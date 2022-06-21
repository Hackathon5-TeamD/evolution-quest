import "./App.css";
import { Router } from "./router/Router";
import { RecoilRoot } from "recoil";

export default function App() {
  return (
    <div className="App">
      <RecoilRoot>
        <Router />
      </RecoilRoot>
    </div>
  );
}
