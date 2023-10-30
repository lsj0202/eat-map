import type { NextApiRequest, NextApiResponse } from "next";
import { StoreApiResponse, StoreType } from "@/interface";
import { Prisma, PrismaClient } from "@prisma/client";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<StoreApiResponse | StoreType[]>
) {
  const { page = "" }: { page?: string } = req.query;
  const prisma = new PrismaClient();

  if (page) {
    const count = await prisma.store.count();
    const skipPage = parseInt(page) - 1;
    const stores = await prisma.store.findMany({
      orderBy: { id: "desc" },
      take: 10,
      skip: skipPage * 10,
    });

    // totalpage, data, page

    res.status(200).json({
      page: parseInt(page),
      data: stores,
      totalCount: count,
      totalPage: count / 10,
    });
  } else {
    const stores = await prisma.store.findMany({
      orderBy: { id: "asc" },
    });

    return res.status(200).json(stores);
  }
}
