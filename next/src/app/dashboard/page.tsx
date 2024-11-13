import TitleWrapper from '@/components/layouts/title-wrapper'
import { BarChartComponent } from '@/components/shared/bar-chart'
import { IconCard } from '@/components/shared/icon-card'
import { Button } from '@/components/ui/button'
import { Card, CardContent, CardHeader } from '@/components/ui/card'
import { CupSoda, DollarSign, } from 'lucide-react'
import Image from 'next/image'
import Link from 'next/link'
import React from 'react'

const data = [
    {
        title: 'Revenue',
        value: '$100,000',
        icon: DollarSign
    },
    {
        title: 'Orders',
        value: '100',
        icon: DollarSign
    },
    {
        title: 'Tip Amount',
        value: '100',
        icon: DollarSign
    },
    {
        title: 'Dishes',
        value: '50',
        icon: CupSoda
    }
]

const orders = [
    {
        title: 'Order #1',
        quantity: '100',
        status: 'Pending',
        image: '/images/1.jpg'
    },
    {
        title: 'Order #2',
        quantity: '100',
        status: 'Pending',
        image: '/images/1.jpg'
    },
    {
        title: 'Order #3',
        quantity: '100',
        status: 'Pending',
        image: '/images/1.jpg'
    },
    {
        title: 'Order #4',
        quantity: '100',
        status: 'Pending',
        image: '/images/1.jpg'
    },
    {
        title: 'Order #5',
        quantity: '100',
        status: 'Pending',
        image: '/images/1.jpg'
    },
]

const DashboardPage = () => {
    return (
        <main className='grid grid-cols-1 md:grid-cols-12 gap-4'>
            <div className='col-start-1 col-end-13'>
                <TitleWrapper title="Dashboard" button={<Button>Add</Button>}>
                    <div className='grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4'>
                        {data.map((item) => (
                            <div
                                key={item.title}
                                className='size-full'
                            >
                                <IconCard
                                    icons={<item.icon />}
                                    title={item.title}
                                    value={item.value}
                                />
                            </div>
                        ))}
                    </div>
                </TitleWrapper>
            </div>
            <div className='col-start-1 col-end-5'>
                <Card className='flex flex-col gap-2'>
                    <CardHeader className='flex flex-row items-center justify-between gap-4'>
                        <h1>Today upSales</h1>
                        <Link
                            href="/orders"
                            className='underline hover:no-underline'
                        >
                            View All
                        </Link>
                    </CardHeader>
                    <CardContent>
                        {orders.map((order) => (
                            <div
                                key={order.title}
                                className='size-full'
                            >
                                <div className="flex items-center justify-start gap-2">
                                    <div className='rounded-full bg-muted-foreground p-4 text-white font-bold size-[2rem] relative overflow-hidden'>
                                        <Image
                                            fill
                                            src={order.image}
                                            alt="order"
                                        />
                                    </div>
                                    <div>
                                        <h1 className="text-md font-semibold">{order.title}</h1>
                                        <h1 className="text-xs">
                                            orders: {order.quantity}
                                        </h1>
                                    </div>
                                </div>
                            </div>
                        ))}
                    </CardContent>
                </Card>
            </div>
            <div className='col-start-5 col-end-13'>
                <BarChartComponent />
            </div>
        </main>
    )
}

export default DashboardPage
