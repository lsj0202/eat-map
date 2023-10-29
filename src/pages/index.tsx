import { useState } from "react";
import Map from "@/components/Map";
import Markers from "@/components/Markers";
import * as stores from "@/data/store_data.json";
import StoreBox from "@/components/StoreBox";
import { StoreType } from "@/interface";

const Home = ({ stores }: { stores: StoreType[] }) => {
  const [map, setMap] = useState(null);
  const [currentStore, setSurrentStore] = useState(null);

  return (
    <>
      <Map setMap={setMap} />
      <Markers stores={stores} map={map} setSurrentStore={setSurrentStore} />
      <StoreBox store={currentStore} setStore={setSurrentStore} />
    </>
  );
};

export default Home;

export async function getStaticProps() {
  const stores = await fetch(
    `${process.env.NEXT_PUBLIC_API_URL}/api/stores`
  ).then((res) => res.json());

  return {
    props: { stores },
    revalidate: 60 * 60,
  };
}
