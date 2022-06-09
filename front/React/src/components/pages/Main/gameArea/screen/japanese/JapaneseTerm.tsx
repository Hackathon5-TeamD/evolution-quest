import styles from "../screen.module.css";

type Props = {
  text: string;
};

export const JapaneseTerm = (props: Props) => {
  const { text } = props;
  return (
    <div>
      <p className={styles.typeTitle}>
        Web3層構造
        <span>
          {/* プレゼンテーション層、アプリケーション層、データ層からなるなんかアレだったりもするんだけどいまいちよくわかってないのでタイピングして覚えたい。なんとなく長文を打って表示のされ方を確認中なので文章に特に意味はないです */}
          {text}
        </span>
      </p>
    </div>
  );
};
