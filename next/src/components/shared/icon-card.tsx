import React from 'react'
import { Card } from '../ui/card'

interface Props {
    icons: React.ReactNode
    title: string
    value: string
}

export const IconCard = (props: Props) => {
    return (
        <Card className="flex flex-col items-center justify-center gap-2 p-4 text-center rounded-xl border-2">
            <div className='rounded-full bg-muted-foreground p-4 text-white font-bold'>
                {props.icons}
            </div>
            <div>
                <h1 className="text-md">{props.title}</h1>
                <h1 className="text-2xl font-bold">
                    {props.value}
                </h1>
            </div>
        </Card>
    )
}
