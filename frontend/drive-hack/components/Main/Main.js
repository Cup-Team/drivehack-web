import styles from "../../styles/Main.module.css";
import axios from "redaxios";
import useSWR from "swr";
import Card from "./Card.js";
import Header from "./Header";

const Main = () => {
  const url = "api/startups/";
  const fetcher = async () => {
    const startups = await axios.get(url);
    return startups.data;
  };
  const { data, _ } = useSWR(url, fetcher);

  if (!data) return <></>;
  return (
      <div className={styles.mainWrapper}>
        {data.map(({ title, description, mentions, media }, index) => (
          <Card
            title={title}
            description={description}
            mentions={mentions}
            media={media}
            key={index}
          />
        ))}
      </div>
  );
};

export default Main;
