type Resp<T, U = {count: number}> = {
    status: number,
    data: T,
    meta: U
}

interface Example {
    name: string
}

interface Resp2<T, U = {count: number}> extends Example {
    status: number,
    data: T,
    meta: U
}

type User = {
    status: number,
    data: {
        name: string
    }
}

let user: User = {
    status: 200,
    data: {
        name: 'Diantya Pitaloka'
    }
}
const userResp: Resp<{ name: string}> = {
    status: 200,
    data: {
        name: 'Diantya Pitaloka'
    }
}

const postResp: Resp<{title: string, content:string}> = {
    status: 200,
    data: {
        title: 'Hello World',
        content: 'Lorem Ipsum Dolor'
    },
    meta: {
        count: 1
    }
}

class Rspns<T> {
    constructor (public data: T) {}

    public send<U>(ob): U): Resp<U> {
        return(
            status: 200,
            data: ob
        )

    }
}
