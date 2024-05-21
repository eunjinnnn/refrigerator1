<script>
    import { Card, Listgroup, Avatar, Button } from 'flowbite-svelte';

    let categories = [
    { id: 1, name: 'VEGETABLES' },
    { id: 2, name: 'DRINKS' },
    { id: 3, name: 'FROZEN FOOD' },
    { id: 4, name: 'ETC' }
  ];

  let item_list = [
    { category: 1, foodname: '양파', volume: '5', unit: '개', expiration_date: '2024-05-24' },
    { category: 1, foodname: '대파', volume: '5', unit: '개', expiration_date: '2024-05-23' },
    { category: 1, foodname: '당근', volume: '5', unit: '개', expiration_date: '2024-05-05' },
    { category: 1, foodname: '양배추', volume: '5', unit: '개', expiration_date: '2024-05-07' },
    { category: 2, foodname: '사이다', volume: '2', unit: 'L', expiration_date: '2024-05-28' },
    { category: 2, foodname: '콜라', volume: '2', unit: 'L', expiration_date: '2024-05-06' },
    { category: 3, foodname: '만두', volume: '2', unit: '개', expiration_date: '2024-05-06' },
    { category: 4, foodname: '다진마늘', volume: '10', unit: '조각', expiration_date: '2025-05-06' },
  ];

  function filteredItems(categoryId) {
    return item_list.filter(item => item.category === categoryId).sort((a, b) => {
        return new Date(a.expiration_date) - new Date(b.expiration_date);
    });
  }

  function isExpired(expiration_date) {
    return new Date(expiration_date) < new Date();
  }
</script>

<Listgroup class="mt-2 container mx-auto" items={categories} let:item>
    <div class="flex justify-between items-center mb-4">
        <p class="text-sm font-bold text-gray-900 truncate dark:text-white">{item.name}</p>
        <a href="/" class="text-sm font-medium text-primary-600 hover:underline dark:text-primary-500"> EDIT </a>
    </div>
    <div class="flex flex-wrap -mx-2">
        {#each filteredItems(item.id) as food}
            <div class="w-1/3 p-1">
                <Card class="w-full relative">
                    <div class="flex-wrap text-center">
                        <div class="text-xs">{food.foodname} {food.volume}{food.unit}</div>
                        <div class="text-xs {isExpired(food.expiration_date) ? 'text-red-500' : ''}">{food.expiration_date}</div>
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

