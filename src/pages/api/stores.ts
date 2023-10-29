import type { NextApiRequest, NextApiResponse } from "next";
import { StoreApiResponse } from "@/interface";
import { Prisma, PrismaClient } from "@prisma/client";

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse<StoreApiResponse>
) {
  const { page = "1" }: { page?: string } = req.query;
  const prisma = new PrismaClient();

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
}
