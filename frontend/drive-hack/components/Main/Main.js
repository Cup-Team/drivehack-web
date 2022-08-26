import axios from "redaxios";
import useSWR from "swr";
import Card from "./Card.js";

const Main = () => {
  const url = "api/startups/";
  const fetcher = async () => {
    const startups = await axios.get(url);
    return startups.data;
  };
  const { data, _ } = useSWR(url, fetcher);

  if (!data) return <></>;
  return (
    <>
      {data.map(({ title, description, mentions, media }, index) => (
        <Card
          title={title}
          description={description}
          mentions={mentions}
          media={media}
          key={index}
        />
      ))}
    </>
  );
};

export default Main;
