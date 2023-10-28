import React, { Dispatch, SetStateAction, useCallback, useEffect } from "react";

interface MarkerProps {
  map: any;
  storeDatas: any[];
  setSurrentStore: Dispatch<SetStateAction<any>>;
}

const Markers = ({ map, storeDatas, setSurrentStore }: MarkerProps) => {
  const loadKakaoMarkers = useCallback(() => {
    if (map) {
      // 식당 데이터 마커 띄우기
      storeDatas?.map((store) => {
        var markerPosition = new window.kakao.maps.LatLng(
          store?.y_dnts,
          store?.x_cnts
        );

        var imageSrc = store?.bizcnd_code_nm
            ? `/images/markers/${store?.bizcnd_code_nm}.png`
            : "/images/markers/default.png",
          imageSize = new window.kakao.maps.Size(40, 40), // 마커이미지의 크기입니다
          imageOption = { offset: new window.kakao.maps.Point(27, 69) }; // 마커이미지의 옵션입니다. 마커의 좌표와 일치시킬 이미지 안에서의 좌표를 설정합니다.

        // 마커의 이미지정보를 가지고 있는 마커이미지를 생성합니다
        var markerImage = new window.kakao.maps.MarkerImage(
            imageSrc,
            imageSize,
            imageOption
          ),
          markerPosition = new window.kakao.maps.LatLng(
            store?.y_dnts,
            store?.x_cnts
          );

        // 마커를 생성합니다
        var marker = new window.kakao.maps.Marker({
          position: markerPosition,
          image: markerImage,
        });

        // 마커가 지도 위에 표시되도록 설정합니다
        marker.setMap(map);

        // 마커 커서가 오버되었을 때 위에 표시할 인포원도우 생성
        var content = `<div class="infowindow">${store?.upso_nm}</div>`; // 인포 윈도우에 표시될 내용

        var customOverlay = new window.kakao.maps.CustomOverlay({
          position: markerPosition,
          content: content,
          xAnchor: 0.6,
          yAnchor: 0.91,
        });

        window.kakao.maps.event.addListener(marker, "mouseover", function () {
          // 마커에 마우스오버 이벤트가 발생하면 커스텀오버레이를 마커위에 표시합니다
          customOverlay.setMap(map);
        });

        // 마커에 마우스아웃 이벤트를 등록합니다
        window.kakao.maps.event.addListener(marker, "mouseout", function () {
          // 마커에 마우스아웃 이벤트가 발생하면 커스텀오버레이를 제거합니다
          customOverlay.setMap(null);
        });

        // 선택한 가게 저장
        window.kakao.maps.event.addListener(marker, "click", function () {
          setSurrentStore(store);
          console.log(store);
        });
      });
    }
  }, [map, storeDatas, setSurrentStore]);
  // 의존성 배열 내부의 값이 변경하지 않는다면 이전 값을 사용 (useCallback)

  useEffect(() => {
    loadKakaoMarkers();
  }, [loadKakaoMarkers, map]);

  return <div></div>;
};

export default Markers;
