<script>
    import { Select, Button } from 'flowbite-svelte';

    let categories = [
        { id: 1, name: 'VEGETABLES' },
        { id: 2, name: 'DRINKS' },
        { id: 3, name: 'FROZEN FOOD' },
        { id: 4, name: 'ETC' }
    ];

    let item_list = [
        { category: 1, foodname: '양파', volume: '5', unit: '개', expiration_date: '2024-05-24', purchase_date: '2024-05-20' },
        { category: 1, foodname: '대파', volume: '5', unit: '개', expiration_date: '2024-05-23',  purchase_date: '2024-05-20' },
        { category: 1, foodname: '당근', volume: '5', unit: '개', expiration_date: '2024-05-05', purchase_date: '2024-05-20' },
        { category: 1, foodname: '양배추', volume: '5', unit: '개', expiration_date: '2024-05-07', purchase_date: '2024-05-20' },
        { category: 2, foodname: '사이다', volume: '2', unit: 'L', expiration_date: '2024-05-28', purchase_date: '2024-05-20' },
        { category: 2, foodname: '콜라', volume: '2', unit: 'L', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
        { category: 3, foodname: '만두', volume: '2', unit: '개', expiration_date: '2024-05-06', purchase_date: '2024-05-20' },
        { category: 4, foodname: '다진마늘', volume: '10', unit: '조각', expiration_date: '2025-05-06', purchase_date: '2024-05-20' },
    ];

    let units = [
        { value: 1, name: '개' },
        { value: 2, name: 'L' },
        { value: 3, name: '조각' }
    ];

    let lists = [];
    let cat_selected = '';
    let unit_selected = '';
    let volume = '';
    let foodname = '';



</script>

<form class = 'flex'>
    <Select id="select-category" bind:value={cat_selected} style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
    <Select id="select-category" bind:value={cat_selected} style='font-size:x-small' size="sm" items={categories} placeholder="Category"/>
</form>