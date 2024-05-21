<script>
    import { Card, Listgroup, Avatar, Button } from 'flowbite-svelte';

    let categories = [
        {
            id: 1,
            name: 'VEGETABLES'
        },
        {
            id: 2,
            name: 'DRINKS'
        },
        {
            id: 3,
            name: 'FROZEN FOOD'
        },
        {
            id: 4,
            name: 'ETC'
        }
    ]

    let item_list = [
        {
            foodname: '양파',
            volume: '5',
            unit: '개',
            expiration_date: '2024-05-03'
        },
        {
            foodname: '대파',
            volume: '5',
            unit: '개',
            expiration_date: '2024-05-04'
        },
        {
            foodname: '당근',
            volume: '5',
            unit: '개',
            expiration_date: '2024-05-05'
        }
    ];
</script>

<Listgroup class = 'mt-2 container mx-auto' items={categories} let:item>
    <div class="flex justify-between items-center mb-4">
        <p class="text-sm font-bold text-gray-900 truncate dark:text-white"> #{item.name} </p>
        <a href="/" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"> EDIT </a>
    </div>
    <div class = 'flex flex-wrap -mx-2'>
        {#each item_list as item}
            <div class="w-1/3 p-2">
                <Card class="w-full relative">
                    <div class="flex-wrap text-center">
                        <div class="text-xs">{item.foodname} {item.volume}{item.unit}</div>
                        <div class="text-xxs">{item.expiration_date}</div>
                    </div>
                </Card>
            </div>
        {/each}
    </div>
</Listgroup>


<div class="flex flex-wrap gap-2">
    <Button size = 'xs' outline color="green" href="/add"> ADD </Button>
    <Button sixe = 'xs' outline color="red" href="/delete"> DELETE </Button>
</div>

