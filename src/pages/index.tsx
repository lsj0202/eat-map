import { useState } from "react";
import Map from "@/components/Map";
import Markers from "@/components/Markers";
import StoreBox from "@/components/StoreBox";
import { StoreType } from "@/interface";
import axios from "axios";

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
  const stores = await axios.get(
    `${process.env.NEXT_PUBLIC_API_URL}/api/stores`
  );

  return {
    props: { stores: stores.data },
    revalidate: 60 * 60,
  };
}
