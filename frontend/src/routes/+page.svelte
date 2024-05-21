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

{#each categories as category}
    <div class ='bg-orange-50 mt-2 mb-2 container mx-auto rounded border-dashed border-lime-950 overflow-hidden'>
        <div class="flex justify-between items-center px-4 py-2">
            <p class="font-serif text-sm font-bold text-lime-950 truncate dark:text-white"># {category.name}</p>
            <div class="flex space-x-2">
                <a href="/add" class="font-serif text-xs font-medium text-primary-600 hover:underline dark:text-primary-500"> ADD </a>
                <a href="/delete" class="font-serif text-xs font-medium text-primary-600 hover:underline dark:text-primary-500"> DEL </a>
            </div>
        </div>
        <div class="border-b border-lime-950 border-opacity-30"></div>
        <div class="flex flex-wrap mt-2">
            {#each filteredItems(category.id) as food}
                <div class="w-1/3 p-1">
                    <Card class="w-full relative bg-white border-1 border-lime-950 rounded-lg">
                        <div class="flex flex-col justify-center items-center">
                            <p class="font-serif text-xs text-lime-950 font-bold whitespace-nowrap">{food.foodname} {food.volume}{food.unit}</p>
                            <p class="{isExpired(food.expiration_date) ? 'text-red-500' : 'text-lime-950'} text-xs">{food.expiration_date}</p>
                        </div>
                    </Card>
                </div>
            {/each}
        </div>
    </div>
{/each}


<!-- <Listgroup class="bg-orange-50 mt-2 mb-2 container mx-auto border-2 border-lime-950" items={categories} let:item>
    <div class="flex justify-between items-center mb-4">
        <p class="font-serif text-sm font-bold text-lime-950 truncate dark:text-white">{item.name}</p>
        <div>
            <a href="/add" class="font-serif text-xs font-medium text-primary-600 hover:underline dark:text-primary-500"> ADD </a>
            <a href="/delete" class="font-serif text-xs font-medium text-primary-600 hover:underline dark:text-primary-500"> DEL </a>
        </div>
        
    </div>
    <div class="flex flex-wrap -mx-2">
        {#each filteredItems(item.id) as food}
            <div class="w-1/3 p-1">
                <Card class="w-full relative bg-white border-1px border-lime-950">
                    <div class="flex-wrap text-center">
                        <div class="font-serif text-xs text-lime-950 font-bold">{food.foodname} {food.volume}{food.unit}</div>
                        <div class="font-serif text-xs {isExpired(food.expiration_date) ? 'text-red-500' : 'text-lime-950'}">{food.expiration_date}</div>
                    </div>
                </Card>
            </div>
        {/each}
    </div>
</Listgroup> -->

