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
        서울시 맛집리스트
      </Link>
      <div className="flex gap-3 items-center px-[18px] py-0 hidden-lg">
        <Link href="/stores" className="cursor-pointer hover:text-gray-500">
          맛집 목록
        </Link>
      </div>
    </div>
  );
};

export default Navbar;
