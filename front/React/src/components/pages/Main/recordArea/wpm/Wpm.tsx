import styles from "../recordItems.module.css";

export const Wpm = ({ wpm }) => {
  return (
    <div className={styles.recordItem}>
      <p>WPM</p>
      <h1>
        {wpm ? wpm : 0}
        <span>/ min</span>
      </h1>
    </div>
  );
};
