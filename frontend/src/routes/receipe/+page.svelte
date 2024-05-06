<script>
    import { Card, Listgroup, Avatar } from 'flowbite-svelte';

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

    let veg_list = [
        {
            name: '양파',
            value: '5',
            unit: '개',
            expiration_date: '2024-05-03'
        },
        {
            name: '대파',
            value: '5',
            unit: '개',
            expiration_date: '2024-05-04'
        },
        {
            name: '당근',
            value: '5',
            unit: '개',
            expiration_date: '2024-05-05'
        }
    ];
</script>

<Listgroup items={categories} let:item>
    <div class="flex justify-between items-center mb-4">
        <!-- <h5 class="text-xl font-bold leading-none text-gray-900 dark:text-white">Latest Customers</h5> -->
        <p class="text-sm font-bold text-gray-900 truncate dark:text-white">
            {item.name}
        </p>
        <a href="/" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"> edit </a>
    </div>
    <Listgroup items={veg_list} let:item>
        <p class="text-xs font-medium text-gray-900 truncate dark:text-white">
            {item.name}
            {item.value}
            {item.unit}
        </p>
        <p class="text-xs text-gray-500 truncate dark:text-gray-400">
            {item.expiration_date}
        </p>
    </Listgroup>

</Listgroup>