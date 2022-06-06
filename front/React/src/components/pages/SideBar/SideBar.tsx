import { slide as Menu } from "react-burger-menu";
import styles from "./SideBar.module.css";
import "./SideBar.css";
import {
  BiHomeAlt,
  BiUser,
  BiMedal,
  BiLogInCircle,
  BiLogOutCircle,
} from "react-icons/bi";

type SidemenuProps = {
  pageWrapId: string;
  outerContainerId: string;
};

export const SideBar = ({ pageWrapId, outerContainerId }: SidemenuProps) => {
  return (
    <Menu>
      <p className={styles.memuTitle}>Menu</p>
      <a className={styles.menuItem} href="/">
        <BiHomeAlt />
        Home
      </a>
      <a className={styles.menuItem} href="/user">
        <BiUser />
        User
      </a>
      <a className={styles.menuItem} href="/result">
        <BiMedal />
        Result
      </a>
      <a className={styles.menuItem} href="/">
        <BiLogInCircle />
        Log in
      </a>
      <a className={`${styles.menuItem} ${styles.logout}`} href="/logout">
        <BiLogOutCircle />
        Log out
      </a>
    </Menu>
  );
};
