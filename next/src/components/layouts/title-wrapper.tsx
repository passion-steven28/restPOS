import React from 'react'

type Props = {
    title: string
    button?: React.ReactNode
    children?: React.ReactNode
}

const TitleWrapper = (props: Props) => {
    return (
        <div className="width-full flex flex-col gap-2">
            <div className='flex items-center justify-between'>
                <h1 className='text-4xl font-bold'>
                    {props.title}
                </h1>
                <div>
                    {props.button}
                </div>
            </div>
            <div>
                {props.children}
            </div>
        </div>
    )
}

export default TitleWrapper