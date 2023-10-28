import Link from "next/link";
import React, { useState } from "react";
import { BiMenu } from "react-icons/bi";
import { AiOutlineClose } from "react-icons/ai";

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="flex justify-between items-center fixed w-full h-[52px] top-0 shadow-sm bg-white z-10">
      <Link
        href="/"
        className="text-blue-800 text-lg font-semibold cursor-pointer px-[18px] py-0"
      >
        NextMap
      </Link>
      <div className="flex gap-3 items-center px-[18px] py-0 hidden-lg">
        <Link href="/stores" className="cursor-pointer hover:text-gray-500">
          맛집 등록
        </Link>
        <Link href="/stores/new" className="cursor-pointer hover:text-gray-500">
          맛집 등록
        </Link>
        <Link
          href="/users/likes"
          className="cursor-pointer hover:text-gray-500"
        >
          찜한 가게
        </Link>
        <Link
          href="/users/login"
          className="cursor-pointer hover:text-gray-500"
        >
          로그인
        </Link>
        {/* moblie button */}
      </div>
      <div
        role="presetation"
        className="hidden cursor-pointer px-[18px] block-lg"
        onClick={() => {
          setIsOpen((value) => !value);
        }}
      >
        {isOpen ? <AiOutlineClose /> : <BiMenu />}
      </div>
      {isOpen && (
        <div className="fixed w-full top-[52px] bg-blue-800 text-white h-screen">
          <div className="flex flex-col gap-[16px] px-[18px] py-[24px]">
            <Link href="/stores" className="text-white">
              맛집 등록
            </Link>
            <Link href="/stores/new" className="text-white hover:text-gray-300">
              맛집 등록
            </Link>
            <Link
              href="/users/likes"
              className="text-white hover:text-gray-300"
            >
              찜한 가게
            </Link>
            <Link
              href="/users/login"
              className="text-white hover:text-gray-300"
            >
              로그인
            </Link>
          </div>
        </div>
      )}
    </div>
  );
};

export default Navbar;
