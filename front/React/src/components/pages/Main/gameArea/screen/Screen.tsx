import styles from "./screen.module.css";

export const Screen = () => {
  return (
    <div className={styles.screenArea}>
      <div>
        <p className={styles.typeTitle}>
          Web3層構造
          <span>
            プレゼンテーション層、アプリケーション層、データ層からなるなんかアレだったりもするんだけどいまいちよくわかってないのでタイピングして覚えたい。なんとなく長文を打って表示のされ方を確認中なので文章に特に意味はないです
          </span>
        </p>
      </div>
      <p className={styles.border}></p>
      <div>
        <p className={styles.typeTitle}>
          Web sannsoukouzou
          <span>
            purezente-syonnsou,apurike-syonnsou,de-tasoukaranaru nannkaare
          </span>
        </p>
      </div>
    </div>
  );
};
